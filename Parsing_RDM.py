import requests, urllib, bs4, re, string
from bs4 import BeautifulSoup
from urllib.parse import quote
import os
import fitz
import numpy as np

class ParsingRDM(object):
    def __init__(self,cookies):
        self.cookies = cookies

    def get_dir_name(self,file_dir):
        base_name = os.path.basename(file_dir)  # 获得地址的文件名
        dir_name = os.path.dirname(file_dir)  # 获得地址的父链接
        return dir_name, base_name

    def pdf_image(self,pdf_name):
        dir_name, base_name = self.get_dir_name(pdf_name)
        dir_name = 'D:\RDM_Download\\PDF_Image\\'
        if not os.path.exists(dir_name):  # 如果保存文件夹不存在就创建文件夹
            os.makedirs(dir_name)
        pdf = fitz.Document(pdf_name)
        for pg in range(0, pdf.pageCount):
            page = pdf[pg]  # 获得每一页的对象
            trans = fitz.Matrix(1.0, 1.0).preRotate(0)
            pm = page.getPixmap(matrix=trans, alpha=False)  # 获得每一页的流对象
            pm.writePNG(dir_name + os.sep + base_name + '.png'.format(pg + 1))  # 保存图片
        pdf.close()

    def gethtmltext(self,Request_method, url, cookies, **Others_data):  # Others_data包括请求数据，请求头
        # 用途一：以get方式获得待处理任务web内容
        # 用途二：以get方式下载技术确认书（保存路径:Others_data['pdfpath']）
        # 用途三：以post方式，进入生产指示单中，获取订单web内容
        # Other_data = {'Referer':'参考链接','User-Agent':'模拟浏览器版本','Requests_data':'请求体内容','pdfpath':'pdf文件完整路径'}
        if Request_method == "get":
            # 删除请求头中多余信息Requests_data,pdfpath
            if 'Requests_data' in Others_data:
                Others_data.pop('Requests_data')
            if 'pdfpath' in Others_data:  # 下载文件
                if Others_data['pdfpath'] != "":
                    try:
                        path = Others_data['pdfpath'] + ".pdf"
                        Others_data.pop('pdfpath')
                        url = quote(url, safe=string.printable)
                        resp = requests.get(url, headers=Others_data, cookies=cookies, timeout=30)
                        resp.raise_for_status()
                        with open(path, "wb") as f:
                            f.write(resp.content)
                        f.close()
                        return 'pdf下载成功'
                    except:
                        print("请求超时")
                        return ''
            else:  # 不下载文件
                try:
                    resp = requests.get(url, headers=Others_data, cookies=self.cookies, timeout=30)
                    # 如果状态不是200，引发HTTPError异常
                    resp.raise_for_status()
                    resp.encoding = resp.apparent_encoding
                    return resp.text
                except:
                    print("请求超时")
                    return ""
        elif Request_method == "post":
            if 'Referer' in Others_data:
                Others_data.pop('Referer')
            if 'pdfpath' in Others_data:
                Others_data.pop('pdfpath')
            if 'Requests_data' in Others_data:
                data = Others_data['Requests_data']
                Others_data.pop('Requests_data')
                try:
                    resp = requests.post(url, headers=Others_data, cookies=cookies, timeout=30, data=data)
                    # 如果状态不是200，引发HTTPError异常
                    resp.raise_for_status()
                    resp.encoding = resp.apparent_encoding
                    return resp.text
                except:
                    print("请求超时")
                    return ""
        else:
            print("请求方式有误")
            return ""

    def getsolist(self,demo,keyWord):
        soup = BeautifulSoup(demo, "html.parser")
        list_row = []
        getsolist = []
        # 进入指定tr标签
        # 注意：soup.find('tr',attrs = {'class':'TaskRow'})  实际查找的是tr标签的children
        for tr in soup.find('tr', attrs={'class': 'TaskRow'}).parent:
            if isinstance(tr, bs4.element.Tag):
                for td in tr.children:
                    if isinstance(td, bs4.element.Tag):
                        if td.string == keyWord:
                            input_id = re.search('"\d{7}"',
                                                 str(td.previous_sibling.previous_sibling.previous_sibling)).group(0)[1:-1]
                            task_tid = re.search('"\d{6}"',
                                                 str(td.previous_sibling.previous_sibling.previous_sibling)).group(0)[1:-1]
                            list_row = tr.text.split('\xa0')[1:]
                            list_row.append(input_id)
                            list_row.append(task_tid)
                            getsolist.append(list_row)

        # 删除重复行
        list_del = []
        list_clu = []
        # range(len（list_so）)为行数
        for i in range(len(getsolist)):
            if i != 0 and getsolist[i][0] in list_clu:
                list_del.append(i)  # 当行内第一个元素在列表list_clu中存在，记录需要删除的行数
            else:
                list_clu.append(getsolist[i][0])  # 当行内第一个元素在列表list_clu中不存在，将新元素添加进list_clu

        getso = np.delete(getsolist, list_del, axis=0)  # 统一删除重复数据行
        return getso

    def getsospec(self,demo):
        # 获取成品料号，机型名称，成品规格描述，so对应技术确认书
        # 字典形式输出:    {'so号':'so对应技术确认书','成品料号':'机型名称,成品规格描述'}
        getsospec = {}
        soup = BeautifulSoup(demo, "html.parser")
        # 获取so对应技术确认书名称
        for tag in soup.find('production_order_m').children:
            if isinstance(tag, bs4.element.Tag):
                if tag.name == 'data':
                    for row in tag.children:
                        if isinstance(row, bs4.element.Tag):
                            if row.attachment.text != '':  # 有技术确认书
                                if row.so_no.text not in getsospec:  # 如果SO号不在字典内(去重复用)
                                    if ';' in row.attachment.text:  # 如果存在多份文件
                                        Sopec = re.search(r'(;|^).*?技术确认书.*.pdf',
                                                          row.attachment.text).group()  # 寻找*技术确认书*.pdf
                                        if ';' in Sopec:  # 如果技术确认在其他文件之后
                                            getsospec[row.so_no.text] = Sopec[1:]  # 删除‘；’
                                        else:  # 如果技术确认书在起始位置
                                            getsospec[row.so_no.text] = Sopec  # Sopec即为返回的正则字符串
                                    else:
                                        getsospec[row.so_no.text] = row.attachment.text
                                else:
                                    getsospec[row.so_no.text] = ''  # 无技术确认书，返回空

        # 获取成品料号，以及成品料号对应机型名称 + 成品规格描述
        for tag in soup.find('production_order_s').children:
            if isinstance(tag, bs4.element.Tag):
                if tag.name == 'data':  # 进入data标签
                    for row in tag.children:  # 在row标签内循环叉查找数
                        if isinstance(row, bs4.element.Tag):
                            if row.prd_no.text not in getsospec and re.match(r'[A-Z,0-9]{18}',
                                                                             row.prd_no.text):  # 如果成品料号不在字典内
                                Model_name = re.search(r'(.*V\d.\d(-[A-Z])?)', row.prd_name.text).group()
                                # {'成品料号':'机型名称,成品规格描述'}
                                getsospec[row.prd_no.text] = Model_name + ',' + row.spc.text  # 创建一个新字典关键字，记录信息

        return getsospec

    def pdfparsing(self,list_so, xml_data, headers, cookies, i):
        # 获取订单参数：pid,tid,so_information
        pid = list_so[i][6]  # 1235553
        tid = list_so[i][7]  # 85525
        so_information = list_so[i][5]  # 制单人:王冬琴,客户代码：C058受订单号：SO191129001,品号:601E628H01TV13002L\n

        # 变更对应so请求体
        xml_data = re.sub(r'\d{7}', pid, xml_data)
        headers['Requests_data'] = xml_data
        headers['Connection'] = 'keep-alive'
        posturl = 'http://rdm.toptech-developer.com:81/bpm/XMLService/DataProvider.aspx'
        # 获取so订单web内容
        spec_web = self.gethtmltext("post", posturl, cookies, **headers)
        sospec = self.getsospec(spec_web)  # 获得成品料号，机型名称，成品规格描述
        print(sospec)

        # 下载技术确认书
        so_no = re.search(r'SO\d{9}', so_information).group()
        so_name = sospec[so_no]  # 获得技术确认书名称
        headers['pdfpath'] = 'D:\RDM_Download\\PDF\\'  # 指定下载PDF的保存路径
        if not os.path.exists(headers['pdfpath']):  # 如果保存文件夹不存在就创建文件夹
            os.makedirs(headers['pdfpath'])
        headers['pdfpath'] = headers['pdfpath'] + so_no  # 指定下载文件pdf完整地址
        # http://172.168.5.151:81/bpm/FileUpload/DownloadFile.aspx?md=task&tid=85408&did=&file=SO191127037+X099%u6280%u672f%u786e%u8ba4%u4e66.pdf(技术确认书名称)
        '''  方案一（存在url转码问题，即使将url转化成上面一行的url，使用python request.get方法时，可通过网抓工具fiddle发现url中%被python转换了，已经不是正确的url）：
        spec_unicode = ''
        for s in sospec[so_no]:
            if 'A' <= s <= 'Z' or 'a' <= s <= 'z' or s == '.' or '0' <= s <= '9':
                spec_unicode = spec_unicode + s
            elif s ==' ':
                spec_unicode = spec_unicode + '+'
            elif s == '+':
                spec_unicode = spec_unicode + '%2B'
            else:
                spec_unicode = spec_unicode + hex(ord(s)).upper().replace('0X', '%u')
    
        so_url = 'http://rdm.toptech-developer.com:81/bpm/FileUpload/DownloadFile.aspx?md=task&tid=' + tid + '&did=&file=' + spec_unicode  # 技术确认书url
        '''
        # 方案二：
        so_url = 'http://rdm.toptech-developer.com:81/bpm/FileUpload/DownloadFile.aspx'
        url_data = {'md': 'task', 'tid': tid, 'did': '', 'file': sospec[so_no]}
        url_data_string = urllib.parse.urlencode(url_data)
        so_url = so_url + '?' + url_data_string

        Res = self.gethtmltext("get", so_url, cookies, **headers)
        self.pdf_image(headers['pdfpath'])


if __name__ == '__main__':
    # 初始化部分参数
    cookie_str = r'ASP.NET_SessionId=kblbkgi1ks52yr3jelwiipfh; .ASPXFORMSAUTH=A3E69BE31570688D3E61743DB6C2D15213701B68DBDF433A2B2F9D8A2A397EF37B7CD3FFF4B0D33BC0F23CDB5C1AD537B747C5C8C9ED4386CEDE6026365E4BF032FC95CD5A73735783939A3239677D161771C229CF12E7EFD4D03D21581E26B0EEF0549B387500FEFA8183DA08571CFCBBEDC3FA'
    #处理cookies
    cookies = {}
    for line in cookie_str.split(';'):
        key, value = line.split('=', 1)
        cookies[key] = value

    rdm = ParsingRDM(cookies)

    xml_data = '''<?xml version='1.0'?>
               <Param>
                    <Method>GetFormProcessData</Method>
                    <PID>1235062</PID>
               </Param>
               '''
    headers = {'Referer': 'http://rdm.toptech-developer.com:81/bpm/PostRequest/Default.aspx',
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36 TheWorld 6', }

    # 获取生产指示单列表list_so(二维列表)
    geturl = 'http://rdm.toptech-developer.com:81/bpm/TaskList/Default.aspx'
    # 获取待处理任务中的web内容
    soweb = rdm.gethtmltext("get", geturl, cookies, **headers)
    # 获取列表：['PO20191129001','生产指示单','刘博鹏由王冬琴代填','2019-11-29 09:52:23','TV电源硬件','制单人:王冬琴,客户代码：C058受订单号：SO191129001,品号:601E628H01TV13002L\n','1235553','85525']
    list_so = rdm.getsolist(soweb,"生产指示单")

    # 获取生产指示单成品料号，机型，成品规格描述
    if len(list_so) != 0:  # 如果列表不为空
        print(list_so)  # 打印列表
        # for i in range(len(list_so)):
        #     # 处理PDF
        #     rdm.pdfparsing(list_so, xml_data, headers, cookies, i)
    else:
        print('无待处理的生产指示单')
