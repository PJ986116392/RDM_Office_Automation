import pandas as pd

class dataAnalysis(object):
    def __init__(self,projectName,projectNum,projectSpec):
        self.projectName = projectName
        self.projectNum = projectNum
        self.projectSpec = projectSpec
        self.io = r'E:\PycharmProjects\RDM_Office_Automation\ExcelLib\dataLib.xlsx'


    def Screen(self,projectName,projectNum,projectSpec):                            # 根据输入字符串，筛选出符合条件的data
        self.projectName = projectName
        self.projectNum = projectNum
        self.projectSpec = projectSpec
        self.data = pd.read_excel(self.io)
        screenList = [self.projectName, self.projectNum, self.projectSpec]          # 输入字符串转为列表，方便循环
        head = ['ProjectName','ProjectNum','ProjectSpec']                           # 输入字符串查找的范围
        data = self.data                                                            # 新建变量，不修改原始数据
        for i,item in enumerate(screenList):
            if len(item) != 0 :                                                     # 如果输入字符串不为空
                item = item.upper()                                                 # 将输入字符串中的小写字母改为大写
                if "&" in item:                                                     # 如果输入字符串需要简单的与逻辑
                    conditions = item.split("&")
                    for condit in conditions:                                       # for循环做逻辑与关系，在第一次基础上再一次筛选
                        data = data.loc[data[head[i]].str.contains(condit)]         # data["A"].str.contains("x") pandas 快速返回A列中包含字符串x的内容
                else:
                    # 情景1:输入字符串没有&，|，如只有单个搜索关键字
                    # 情景2:输入字符串中包含|，data["A"].str.contains("x") 函数能够自动识别“|”，做逻辑或的关系
                    data = data.loc[data[head[i]].str.contains(item)]
        return data


if __name__ == '__main__':
    data = dataAnalysis('p65&53','','')
    data = data.Screen('p65&53','','AV&Ypbpr')
    print(data.shape)