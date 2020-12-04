import pandas as pd
import os

class dataAnalysis(object):
    def __init__(self,projectName,projectNum,projectSpec):
        self.projectName = projectName
        self.projectNum = projectNum
        self.projectSpec = projectSpec
        # 获取项目文件路径
        self.io = str(os.path.abspath(os.path.join(os.getcwd(), "../"))) + '\ExcelLib'


    def Screen(self,projectName,projectNum,projectSpec,fileName):                            # 根据输入字符串，筛选出符合条件的data
        sourceData = self.getSourcedata(fileName)
        dataFilter = self.lookFordata(projectName,projectNum,projectSpec,sourceData)
        return dataFilter.values,dataFilter.columns.values

    def getFilepath(self,fileName):
        return self.io + '\\' + fileName + '.xls'

    def getSourcedata(self,fileName):
        filePath = self.getFilepath(fileName)
        return pd.read_excel(filePath)

    def lookFordata(self,projectName,projectNum,projectSpec,sourceData):
        ###################################################################################################################
        #######################     由于注意事项以及料号规格库，不定期更新，故将其放在两个sheet中，方便管理      ######################
        ###################################################################################################################
        # # 存储每个料号注意事项，不定期更新
        # waring_data = pd.read_excel(self.io, sheet_name="WaringInformation")
        # # 由于暂时无法直接连上金蝶，只能定期更新本地库文件，文件中存储当前最新的料号与规格，会不定期更新
        # lib_data = pd.read_excel(self.io,sheet_name="Lib")
        #
        # # 根据料号，项目名称合并datafarme，采用outer方式，其他无注意事项的填充NAN
        # data = pd.merge(lib_data,waring_data,on = ['ProjectNum','ProjectName'],how = "outer")

        self.projectName = projectName
        self.projectNum = projectNum
        self.projectSpec = projectSpec
        data = sourceData

        # 根据输入信息搜索数据
        screenList = [self.projectName, self.projectNum, self.projectSpec]          # 输入字符串转为列表，方便循环
        head = ['ProjectName','ProjectNum','ProjectSpec']                           # 输入字符串查找的范围
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

        # # dataFrame 排序sort_values by参数可以指定根据哪一列数据进行排序,na_position='last' 将空值排在最后,ascending是设置升序和降序
        # data = data.sort_values(by = "waringInformation",ascending=False)
        # # data.isnull 查找空值，np.where 返回nympy 数据，分别记录行，列
        # # 参考 https://blog.csdn.net/alanguoo/article/details/77198503
        # nanRow = np.where(data.isnull())[0][0]
        #
        # dataFilter = data.iloc[:,:-1]
        #
        # # data.ProjectNum.values 数据类型为numpy
        # data1 = list(data.ProjectNum.values)
        # # data.iloc[:, -1].values 数据类型为numpy
        # data2 = list(data.iloc[:, -1].values)
        #
        # Waring_data = dict(zip(data1,data2))

        return data


    def deldata(self,sourceData,delList):
        resultData = sourceData[~sourceData['ProjectNum'].isin(delList)]
        filePtah = self.getFilepath('WaringInformation')
        resultData.to_excel(filePtah,sheet_name="WaringInformation",index=False)

if __name__ == '__main__':
    data = dataAnalysis('','','')
    data = data.Screen('12AT07','','','WaringInformation')
