from tkinter import *
import requests
class Application(Frame):
    def __init__(self,master = None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.creatwidget()


    def creatwidget(self):
        # 登录界面
        # 用户名称
        # 方法一
        """"
        self.loginLabel = Label(self,text = "登录（Login...)",bg = "deepskyblue",
                                fg = "white",font = ("微软雅黑",9),width = 49,anchor = "w")
        self.loginLabel.pack()

        self.text = Text(self,width = 49 , height = 6)
        self.text.pack()

        self.text.insert("1.0", "            账号:")
        self.userName = StringVar()
        userNameinput = Entry(self, textvariable = self.userName)
        self.userName.set("pengjian")
        self.text.window_create(INSERT, window=userNameinput)

        self.text.insert("2.0", "\n            密码:")
        self.pwd = StringVar()
        passWord = Entry(self, textvariable = self.pwd)
        self.pwd.set("")
        self.text.window_create(INSERT, window=passWord)

        loginBtn = Button(self, text=" 登录 ", command=self.Login)
        cannelBtn = Button(self, text=" 取消 ", command=root.destroy)
        self.text.insert("insert","\n                         ")
        self.text.window_create(INSERT, window=loginBtn)
        self.text.window_create(INSERT, window=cannelBtn)

        """
        Label(self, text="登录（Login...)", bg="deepskyblue",fg="white", font=("微软雅黑", 9), width=49, height = 1,anchor="w",pady = 2)\
            .grid(row = 1,column = 0 ,columnspan = 5)
        Label(self,text = "账号:").grid(row = 2,column = 1,sticky = EW)
        Label(self, text="密码:").grid(row=3, column = 1,sticky = EW)

        self.userName = StringVar()
        Entry(self, textvariable = self.userName).grid(row = 2,column = 2,columnspan = 2,sticky = W,pady = 10)
        self.userName.set("pengjian")

        self.pwd = StringVar()
        Entry(self, textvariable = self.pwd).grid(row = 3,column = 2,columnspan = 2,sticky = W)
        self.pwd.set("")

        Button(self, text=" 登录 ", command=self.Login).grid(row = 4,column = 3,sticky = W)
        Button(self, text=" 取消 ", command=root.destroy).grid(row = 4,column =3,sticky = E)


    def Login(self):
        url = "http://rdm.toptech-developer.com:81/BPM/Home/Login.aspx?ReturnUrl=/bpm/TaskList/Default.aspx"
        data ={
            'Login1$_txtAccount': self.userName.get(),
            'Login1$_txtPWD':'',
            '__VIEWSTATE':'/wEPDwUKLTQ1NTkwODAyMg9kFgICAw9kFgQCAQ9kFg4CBQ8PFgIeBFRleHQFM+W9k+WJjTxmb250IGNvbG9yPSIjY2MwMDAwIj4xPC9mb250PuS9jeeUqOaIt+WcqOe6v2RkAgcPDxYCHwAFBzxiPjwvYj5kZAIJDw8WAh4HVmlzaWJsZWhkZAIKDw8WBB8ABQXCoHzCoB8BaGRkAgsPDxYEHwAFBuWkluWHuh4LTmF2aWdhdGVVcmwFFC4uL0NvbW1vbi9MZWF2ZS5hc3B4ZGQCDQ8PFgIfAAUG5biQ5Y+3ZGQCDw8PFgIfAAUG6YCA5Ye6ZGQCAw9kFgICBA8PFgIfAAUb55So5oi35ZCN5oiW5a+G56CB5pyJ6K+v77yBZGRktThqfHvDjJayCu2Ywmisa6gVkQk=',
            '__EVENTVALIDATION':'/wEWBQLupKneDAKTup+7CgKdu4mlDQLzuILQCgLbqb+1DIuL2a5Sf0hGICaCq32juFgb4ssf',
            'Login1$_btnWebLogin':'登录(zh-chs)'
        }
        resp = requests.post(url,data)
        resp.raise_for_status()
        if resp.status_code == 200:
            resp.encoding = resp.apparent_encoding
            return resp.text


if __name__ == '__main__':
    root = Tk()
    rootWidth = 350
    rootHeight = 125
    # 获取屏幕分辨率
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()
    # 计算出偏移坐标
    x = (screenWidth - rootWidth)/2
    y = (screenHeight - rootHeight)/2
    root.geometry("%dx%d+%d+%d"%(rootWidth,rootHeight,x,y))
    root.title("Top-tech RDM V1.0")
    app = Application(master=root)
    app.mainloop()