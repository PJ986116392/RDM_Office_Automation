import requests, urllib, bs4, re, string
from bs4 import BeautifulSoup
from urllib.parse import quote
import os,fitz
import numpy as np
import xml.etree.ElementTree as ET

class WebText(object):                          # 爬虫技术类
    def __init__(self,webtext,cookies):
        self.webtext = webtext
        self.cookies = cookies

    def getCookie(self,url, account, pwd):
        # 获取cookie函数，如果用户名，密码错误，errorFlag返回False，并且cookie为空
        errorFlag = False
        data = {
            'Login1$_txtAccount': account,
            'Login1$_txtPWD': pwd,
            '__VIEWSTATE': '/wEPDwUKLTQ1NTkwODAyMg9kFgICAw9kFgQCAQ9kFg4CBQ8PFgIeBFRleHQFM+W9k+WJjTxmb250IGNvbG9yPSIjY2MwMDAwIj4xPC9mb250PuS9jeeUqOaIt+WcqOe6v2RkAgcPDxYCHwAFBzxiPjwvYj5kZAIJDw8WAh4HVmlzaWJsZWhkZAIKDw8WBB8ABQXCoHzCoB8BaGRkAgsPDxYEHwAFBuWkluWHuh4LTmF2aWdhdGVVcmwFFC4uL0NvbW1vbi9MZWF2ZS5hc3B4ZGQCDQ8PFgIfAAUG5biQ5Y+3ZGQCDw8PFgIfAAUG6YCA5Ye6ZGQCAw9kFgICBA8PFgIfAAUb55So5oi35ZCN5oiW5a+G56CB5pyJ6K+v77yBZGRktThqfHvDjJayCu2Ywmisa6gVkQk=',
            '__EVENTVALIDATION': '/wEWBQLupKneDAKTup+7CgKdu4mlDQLzuILQCgLbqb+1DIuL2a5Sf0hGICaCq32juFgb4ssf',
            'Login1$_btnWebLogin': '登录(zh-chs)'
        }
        # allow_redirects 重定向使能，一般登录时，用户端会将用户名，密码等信息上传至服务器，服务器返回cookie，或者令牌token 给用户端
        # 返回方式为重定向，用抓包工具可知此时状态码为302 ， request库默认 allow_redirects=Ture 允许自动重定向，resp得到的是重定向之后的200的HTML内容
        resp = requests.post(url, data, allow_redirects=False, timeout=30)
        resp.raise_for_status()
        if resp.status_code == 302:
            # 查看网页，寻找规律发现302，为用户名，密码正确，且服务器设置用户端cookie
            resp.encoding = resp.apparent_encoding
            # str = requests.utils.dict_from_cookiejar(resp.cookies)              # 获取cookie字符串
            # # 组合成字符串字典
            # cookies = {}
            # for line in str.split(';'):
            #     key, value = line.split('=', 1)
            #     cookies[key] = value
            #
            errorFlag = True
            return errorFlag, requests.utils.dict_from_cookiejar(resp.cookies)
        elif resp.status_code == 200:
            # 分析网页可得，状态码为200时，用户名或者密码错误
            errorFlag = False
            return errorFlag, ''

    def gethtmltext(self,Request_method, url, **Others_data):  # Others_data包括请求数据，请求头
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
                        resp = requests.get(url, headers=Others_data, cookies=self.cookies, timeout=30)
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
                    resp = requests.post(url, headers=Others_data, cookies=self.cookies, timeout=30, data=data)
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
        pid,tid,getsolist = [],[],[]
        # 进入指定tr标签
        # 注意：soup.find('tr',attrs = {'class':'TaskRow'})  实际查找的是tr标签的children
        for tr in soup.find('tr', attrs={'class': 'TaskRow'}).parent:
            if isinstance(tr, bs4.element.Tag):
                for td in tr.children:
                    if isinstance(td, bs4.element.Tag):
                        if td.string == keyWord:
                            input_id = re.search('"\d{7}"',
                                                 str(td.previous_sibling.previous_sibling.previous_sibling)).group(0)[1:-1]
                            task_tid = re.search('"\d{5,6}"',
                                                 str(td.previous_sibling.previous_sibling.previous_sibling)).group(0)[1:-1]
                            list_row = tr.text.strip().split('\xa0')
                            list_row.append(input_id)
                            list_row.append(task_tid)
                            getsolist.append(list_row)

        # 删除重复行
        list_del,list_clu = [],[]
        # range(len（list_so）)为行数
        for i in range(len(getsolist)):
            if i != 0 and getsolist[i][0] in list_clu:
                list_del.append(i)  # 当行内第一个元素在列表list_clu中存在，记录需要删除的行数
            else:
                list_clu.append(getsolist[i][0])  # 当行内第一个元素在列表list_clu中不存在，将新元素添加进list_clu
        # 获取列表：['PO20191129001','生产指示单','刘博鹏由王冬琴代填','2019-11-29 09:52:23','TV电源硬件','制单人:王冬琴,客户代码：C058受订单号：SO191129001,品号:601E628H01TV13002L\n','1235553','85525']
        getso = np.delete(getsolist, list_del, axis=0)  # 统一删除重复数据行
        for data in getso:
            pid = pid.append(data[6])
            tid = tid.append(data[7])

        return getso,pid,tid

    def getSoinformation(self,url,pid):
        if len(pid) > 0:
            header = {'Referer': 'http://rdm.toptech-developer.com:81/bpm/PostRequest/Default.aspx',
                      'Content-Type':'text/xml; charset=UTF-8',
                      'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36 TheWorld 6', }
            xml_data = '''<?xml version='1.0'?>
                       <Param>
                            <Method>GetFormProcessData</Method>
                            <PID>1235062</PID>
                       </Param>
                       '''
            if re.search(r'\d{5,7}',xml_data):
                xml_data = re.sub(r'\d{5,7}',pid,xml_data)
                xml_data = xml_data.encode('utf-8')

                try:
                    resp = requests.post(url, headers=header, cookies=self.cookies, timeout=30, data=xml_data)
                    # 如果状态不是200，引发HTTPError异常
                    resp.raise_for_status()
                    resp.encoding = resp.apparent_encoding
                    # webText 数据为xml格式
                    # xml 数据格式化url：https://tool.ip138.com/xml/
                    webText = resp.text

                    # 方案一：正则表达式处理xml数据
                    # keyword = keyWord_dic.keys()
                    # for key in keyword:
                    #     keyvalue = keyWord_dic[key]
                    #     startIndex = len(keyvalue) + 2
                    #     endIndex = -(len(keyvalue)+3)
                    #
                    #     #<变量名>.*</变量名>
                    #     regex = re.compile(r'<' + keyvalue + '>.*</' + keyvalue +'>')
                    #     # findall后数据格式
                    #     # ['<Qty>362.0000</Qty>', '<Qty>361.0000</Qty>', '<Qty>362.0000</Qty>', '<Qty>1.0000</Qty>']
                    #     if regex.search(webText,re.M):
                    #         reslut = regex.findall(webText,re.M)
                    #         for data,index in enumerate(reslut):
                    #             reslut[index] = data[startIndex:endIndex]
                    #         print(reslut)


                    # 方案二：xml.etree.ElementTree 模块处理xml数据
                    # https://www.cnblogs.com/xiaobingqianrui/p/8405813.html
                    xmlFilePath = os.path.abspath("test.xml")
                    try:
                        tree = ET.parse(xmlFilePath)
                        # 获得根节点
                        root = tree.getroot()
                        # captionList = root.iterfind()
                        #("Production_Order_M")
                        # for caption in captionList:
                        #     if caption.tag == "Data":
                        #         for data in :
                        #             if data =="Customer"
                        #                 print(data.arr)
                        #             elif data == ""
                        #                 pass
                    except Exception as e:  # 捕获除与程序退出sys.exit()相关之外的所有异常
                        print("parse test.xml fail!")

                except:
                    print("请求超时")
                    return ""
        else:
            print("pid为空")


    # def getTasklist_text(self,url,keyWord):
    #
    #     list_so = []
    #
    #
    #     headers = {'Referer': 'http://rdm.toptech-developer.com:81/bpm/PostRequest/Default.aspx',
    #                'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36 TheWorld 6', }
    #
    #     # 获取生产指示单列表list_so(二维列表)
    #     #geturl = 'http://rdm.toptech-developer.com:81/bpm/TaskList/Default.aspx'
    #     # 获取待处理任务中的web内容
    #     webText = self.gethtmltext("get", url, self.cookies, **headers)
    #
    #     sort_list = ['生产指示单','BOM制作指导单','(新)ECN变更申请表','异常工艺改善反馈表','生产通知单']
    #
    #     # 获取列表：['PO20191129001','生产指示单','刘博鹏由王冬琴代填','2019-11-29 09:52:23','TV电源硬件','制单人:王冬琴,客户代码：C058受订单号：SO191129001,品号:601E628H01TV13002L\n','1235553','85525']
    #     list_so = self.getsolist(webText, keyWord)
    #     #list_bom = self.getsolist(webText, "BOM制作指导单")
    #     #list_ecn = self.getsolist(webText, "(新)ECN变更申请表")
    #     #list_improvePro = self.getsolist(webText, "异常工艺反馈改善表")
    #
    #     return list_so,webText

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

class PDF():                                # 文件操作，文件（PDF）下载

    def __init__(self):
        pass

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

    def pdfparsing(self, list_so, xml_data, headers, cookies, i):
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
    # 例一：熟悉match
    # s = '23432werwre2342werwrew'
    # p = r'(\d*)([a-zA-Z]*)'
    # m = re.match(p, s)

    # 例二：正则表达式包含变量
    # url = "oreilly.com"
    # regex3 = re.compile(r"^(/|.)*(%s)" % url)       # re.compile(r’表达式( % s)表达式’ % 变量)
    # regex4 = re.compile(r"^(/|.)*oreilly.com")
    # regex5 = re.compile(r"^(/|.)*" + url)           # re.compile(r’表达式’+变量 +’表达式’)
    #
    # string3 = '/oreilly.com/baidu.com'
    #
    # mo3 = regex3.search(string3)
    # mo4 = regex4.search(string3)
    # mo5 = regex5.search(string3)
    #
    # print(mo3.group())
    # print(mo4.group())
    xmlFilePath = os.path.abspath("xml.xml")
    try:
        tree = ET.parse(xmlFilePath)
        # 获得根节点
        root = tree.getroot()
        captionList = root.getchildren()
        for caption in captionList:
            if caption.tag == 'Global':
                stepName = caption.iter('StepName')
                for step in stepName:
                    if step.text == "TV硬件项目经理":
                        print("当前进度为TV硬件项目经理")

            elif caption.tag == "Production_Order_M":
                captionData = caption.find('Data')
                captionRow = captionData.find('Row')
                # print(type(captionRow))
                for value in captionRow.getchildren():
                    # print(value.tag)
                    if value.tag == 'Customer':             # 客户代码
                        print(value.tag,value.text)
                    elif value.tag == 'Attachment':         # 附件名称
                        print(value.tag,value.text)
                    elif value.tag == 'SO_NO':              # 订单so号
                        print(value.tag,value.text)
                    elif value.tag == 'Business_Rem':       # 业务备注
                        print(value.tag,value.text)
                    elif value.tag == 'Make_DD':            # 制单日期
                        print(value.tag,value.text)
                    elif value.tag == 'Make_Man':           # 商务
                        print(value.tag,value.text)
                    elif value.tag == 'Business':           # 业务员
                        print(value.tag,value.text)

            elif caption.tag == 'Production_Order_S':
                captionData = caption.find('Data')
                captionRow = captionData.find('Row')
                for row in captionRow.getchildren():
                    if row.tag == 'Prd_no':
                        if len(row.text) == 18 :        # bom成品料号






    except Exception as e:  # 捕获除与程序退出sys.exit()相关之外的所有异常
        print("parse test.xml fail!")
