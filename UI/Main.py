from UI.Sources.py.loginPanel import LoginPanel
from UI.Sources.py.tasklistPanel import TaskList
import requests
from PyQt5.Qt import *
from Parsing_RDM import ParsingRDM

def getCookie(url,account,pwd):
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
    resp = requests.post(url,data,allow_redirects=False,timeout=30)
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
        return errorFlag,requests.utils.dict_from_cookiejar(resp.cookies)
    elif resp.status_code ==200:
        # 分析网页可得，状态码为200时，用户名或者密码错误
        errorFlag = False
        return errorFlag,''

def getTasklist_text(cookies,url):

    list_so = []
    rdm = ParsingRDM(cookies)

    xml_data = '''<?xml version='1.0'?>
               <Param>
                    <Method>GetFormProcessData</Method>
                    <PID>1235062</PID>
               </Param>
               '''
    headers = {'Referer': 'http://rdm.toptech-developer.com:81/bpm/PostRequest/Default.aspx',
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36 TheWorld 6', }

    # # 获取生产指示单列表list_so(二维列表)
    # geturl = 'http://rdm.toptech-developer.com:81/bpm/TaskList/Default.aspx'
    # 获取待处理任务中的web内容
    soweb = rdm.gethtmltext("get", url, cookies, **headers)
    # 获取列表：['PO20191129001','生产指示单','刘博鹏由王冬琴代填','2019-11-29 09:52:23','TV电源硬件','制单人:王冬琴,客户代码：C058受订单号：SO191129001,品号:601E628H01TV13002L\n','1235553','85525']
    list_so = rdm.getsolist(soweb,"生产指示单")

    return list_so
    # 获取生产指示单成品料号，机型，成品规格描述
    # if len(list_so) != 0:  # 如果列表不为空
    #     print(list_so)
    #     for i in range(len(list_so)):
    #         # 处理PDF
    #         rdm.pdfparsing(list_so, xml_data, headers, cookies, i)
    # else:
    #     print('无待处理的生产指示单')


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    loginpanel = LoginPanel()
    tasklistpanel = TaskList()
    extranetlUrl = {
        'login': 'http://rdm.toptech-developer.com:81/BPM/Home/Login.aspx?ReturnUrl=/bpm/TaskList/Default.aspx',
        'taskList': 'http://rdm.toptech-developer.com:81/bpm/TaskList/Default.aspx',
        'newTask': '',
    }

    # 槽函数
    def login(account,pwd):
        errorFlag, Cookies = getCookie(extranetlUrl["login"],account,pwd)
        if errorFlag == True :
            loginpanel.hide()
            tasklisttext = getTasklist_text(Cookies,extranetlUrl["taskList"])
            print(tasklisttext)
            tasklistpanel.show()
        else:
            print("用户名或密码错误！")


    #信号连接
    loginpanel.check_login_Btn_signal.connect(login)

    loginpanel.show()
    sys.exit(app.exec_())



