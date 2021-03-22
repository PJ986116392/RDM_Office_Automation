import pandas as pd
import numpy as np
import os,re
from datetime import datetime

class dataAnalysis(object):
    def __init__(self,projectName,projectNum,projectSpec):
        self.projectName = projectName
        self.projectNum = projectNum
        self.projectSpec = projectSpec
        # 获取项目文件路径
        self.io = str(os.path.abspath(os.path.join(os.getcwd(), "../"))) + '\ExcelLib'

    def Screen(self,projectName,projectNum,projectSpec,fileName):                            # 根据输入字符串，筛选出符合条件的data
        sourceData = self.getSourcedata(fileName,'')
        dataFilter = self.lookFordata(projectName,projectNum,projectSpec,sourceData)
        return dataFilter.values,dataFilter.columns.values

    def getFilepath(self,fileName,sheetName):
        if len(sheetName)>0:
            return self.io + '\\so_Information\\' + fileName + '.xls'
        else:
            return self.io + '\\' + fileName + '.xls'

    def getSourcedata(self,fileName,sheetName):
        filePath = self.getFilepath(fileName,sheetName)
        return pd.read_excel(io=filePath)

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

        # 根据输入信息搜索数据
        screenList = [projectName, projectNum, projectSpec]          # 输入字符串转为列表，方便循环
        head = ['ProjectName','ProjectNum','ProjectSpec']                           # 输入字符串查找的范围
        for i,item in enumerate(screenList):
            if len(item) != 0 :                                                     # 如果输入字符串不为空
                if i == 0:
                    item = item.upper()                                             # 将输入字符串中的小写字母改为大写
                if "&" in item:                                                     # 如果输入字符串需要简单的与逻辑
                    conditions = item.split("&")
                    for condit in conditions:                                       # for循环做逻辑与关系，在第一次基础上再一次筛选
                        sourceData = sourceData.loc[sourceData[head[i]].str.contains(condit)]         # data["A"].str.contains("x") pandas 快速返回A列中包含字符串x的内容
                else:
                    # ----------------------------------       方案一     ----------------------------------
                    # 情景1:输入字符串没有&，|，如只有单个搜索关键字
                    # 情景2:输入字符串中包含|，data["A"].str.contains("x") 函数能够自动识别“|”，做逻辑或的关系
                    # sourceData = sourceData.loc[sourceData[head[i]].str.contains(item)]                                   # 不能区分字符串中大小写

                    # ----------------------------------       方案二     ----------------------------------
                    # sourceData = sourceData.loc[[True if item in i else False for i in sourceData[head[i]].values]]       # 同方案一
                    # pd.loc(list)   list 必须为Bool类型列表或者合法的index表达式，当为bool list时，自动删除为False的数据

                    # ----------------------------------       方案二     ----------------------------------
                    filterList = []
                    for data in sourceData[head[i]].values:
                        #data = str(data).upper()
                        filterList.append(bool(re.search(item, data, re.IGNORECASE)))
                    sourceData = sourceData.loc[filterList]

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

        return sourceData

    def deldata(self,sourceData,delList):
        resultData = sourceData[~sourceData['ProjectNum'].isin(delList)]
        filePtah = self.getFilepath('WaringInformation','')
        resultData.to_excel(filePtah,sheet_name="WaringInformation",index=False)

    def add_data(self,addData):
        pd_data = pd.DataFrame(addData,columns=['ProjectName','ProjectNum','waringInformation'])
        filePtah = self.getFilepath('WaringInformation','')
        sourcedata = self.getSourcedata('WaringInformation','')
        pd_data = sourcedata.append(pd_data)
        pd_data.to_excel(filePtah,sheet_name="WaringInformation",index=False)

    def solist_to_excel(self,list,backlist):
        # 获取当前文件夹内年份excel文件名信息
        dirPath = self.io + '\\' + 'so_Information'
        if not os.path.exists(dirPath):  # 如果保存文件夹不存在就创建文件夹
            os.makedirs(dirPath)
        fileList = []
        files = os.listdir(dirPath)  # 得到文件夹下的所有文件名称
        for file in files:
            index = file.rfind('.')
            file = file[:index]
            fileList.append(file)

        Col = ['客户代码','附件名称','SO号','业务备注','制单时间','制单人员','业务员','成品名称','成品料号','成品规格','订单数量','当前步骤','PID']
        for i in range(np.array(backlist).shape[1]):
            Col.append("退回人员" + str(i+1))
        # 获取合并当前订单数据
        A = np.array(list)
        B = np.array(backlist)
        if A.shape[0] == B.shape[0]:                # 如果两者行数相等
            merge_data = np.append(A, B, axis=1)
            Sourcedata = pd.DataFrame(merge_data,columns=Col)
            Sourcedata['制单时间'] = pd.to_datetime(Sourcedata['制单时间'])

            # 将数据按照年分类保存
            Years = []
            for index,Date in enumerate(Sourcedata['制单时间']):
                if Date.strftime("%Y") not in Years:
                    Years.append(Date.strftime("%Y"))
                Sourcedata.loc[index,'年']=Date.strftime("%Y")
            for year in Years:
                saveData = Sourcedata[Sourcedata['年'] == year]
                saveData.pop('年')
                fileName = dirPath + '\\' + year + '.xls'
                if year not in fileList:            # 年份excel文件不存在
                    pd.DataFrame(saveData).to_excel(fileName, index=False)
                else:                               # 年份excel文件存在
                    initdata = pd.read_excel(fileName)
                    # 当前需要保存的数据中是否有重复so
                    for so in saveData['SO号']:
                        if so in initdata['SO号'].values:  # 当前保存的so在已有excel中
                            saveData = saveData[saveData['SO号'] != so]
                    if not saveData.empty:
                        # 两个pd 去重复，仅仅保留新增的数据
                        # https://www.cnblogs.com/johnyang/p/12849351.html
                        intidata_col = initdata.columns
                        saveData_col = saveData.columns
                        saveData_col = saveData_col.append(intidata_col)
                        saveData_col = saveData_col.append(intidata_col)
                        dif_col = saveData_col.drop_duplicates(keep=False)
                        if len(dif_col.values)>0:           # 有新增退回人员
                            for back in dif_col:
                                initdata[back] = None
                            initdata = initdata.append(saveData, ignore_index=True)  # ignore_index=True,表示不按原来的索引，从0开始自动递增
                            pd.DataFrame(initdata).to_excel(fileName, index=False)
                        else:                               # 无新增退回人员
                            initdata = initdata.append(saveData, ignore_index=True)  # ignore_index=True,表示不按原来的索引，从0开始自动递增
                            pd.DataFrame(initdata).to_excel(fileName, index=False)

if __name__ == '__main__':
    # print('通过字典创建DataFrame:')
    # df_1 = pd.DataFrame({'A': 1.0,
    #                      'B': pd.Timestamp(2019, 8, 19),
    #                      'C': pd.Series(1, index=list(range(4)), dtype='float32'),
    #                      'D': np.array([3] * 4, dtype='int32'),
    #                      'E': pd.Categorical(['test', 'train', 'test', 'train']),
    #                      'F': 'foo'})
    # # print(df_1[['D', 'E', 'F']])
    # print(df_1.columns)
    # df_1.pop('E')
    # print(df_1.columns)
    # # print(df_1[df_1['E']=='test'])

    # a = pd.Series(['客户代码','附件名称','SO号','back1','back2'])
    # b = pd.Series(['客户代码', '附件名称', 'SO号', 'back1', 'back3'])
    # b = b.append(a)
    # b = b.append(a)
    # dif = b.drop_duplicates(keep=False)
    # if len(dif.values)>0 :
    #     print(dif)

    # data_a = {'state': [1, 1, 2], 'pop': ['a', 'b', 'c']}
    # data_b = {'state': [1, 2, 3], 'pop': ['b', 'c', 'd'],'C':['AAAA','AAAAA']}
    # a = pd.DataFrame(data_a)
    # b = pd.DataFrame(data_b)
    # print(a.append(b))
    pass
