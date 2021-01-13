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
        sourceData = self.getSourcedata(fileName)
        dataFilter = self.lookFordata(projectName,projectNum,projectSpec,sourceData)
        return dataFilter.values,dataFilter.columns.values

    def getFilepath(self,fileName,sheetName):
        if len(sheetName)>0:
            return self.io + '\\so_Information\\' + fileName + '.xls'
        else:
            return self.io + '\\' + fileName + '.xls'

    def getSourcedata(self,fileName,sheetName):
        filePath = self.getFilepath(fileName,sheetName)
        if len(sheetName)>0:                                           # 如果sheetName存在
            return pd.read_excel(io = filePath,sheet_name=sheetName)
        else:
            return pd.read_excel(io = filePath)

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
        filePtah = self.getFilepath('WaringInformation')
        resultData.to_excel(filePtah,sheet_name="WaringInformation",index=False)

    def add_data(self,addData):
        pd_data = pd.DataFrame(addData,columns=['ProjectName','ProjectNum','waringInformation'])
        filePtah = self.getFilepath('WaringInformation')
        sourcedata = self.getSourcedata('WaringInformation')
        pd_data = sourcedata.append(pd_data)
        pd_data.to_excel(filePtah,sheet_name="WaringInformation",index=False)

    def solist_to_excel(self,list,backlist):
        # [['C001', 'SO210113012+C001技术确认书.pdf', 'SO210113012', '主芯片 软件客供，PCB不下单', '2021-01-13 15:20:43', '冯瑞霞', '易子弦',
        #   'EL.MT6683-A75(36-42V/300MA,C001,美国,认证管控)', '601ELMT6683A75008L',
        #   'AC 100-240V/50/60HZ 宽电压输入安卓三合一板卡，40W高压(BYQ250),背光参数36-42V/300MA,2路2pin 2.0立式并联背光接口,软件控制电流,主芯片MSD6683BQH-8-00E9(带DD,RAM 512M),外置DDR3 256M,EMMC 4G,ATV制式：NTSC,DTV制式：ATSC,30PIN 2.0mm LVDS插针型屏接口(空第6PIN),驱屏电压12V,支持14PIN 2.0mm按键板接口,支持4PIN 2.54mm喇叭接口,功放供电电压12V,支持7PIN 1.25mm WIFI接口,支持2PIN 2.0mm 12V电源接口,1路RJ45网络输入,3路HDMI输入,1路AV输入（RCA）,1路RF输入(螺纹头),2路USB2.0输入,1路光纤输出,1路耳机输出,（C001,美国）',
        #   2842.0, 'TV电源项目经理', '1741885'],
        #  ['C001', 'SO210113013+C001技术确认书.pdf', 'SO210113013', '芯片 软件客供，物料挪SO201217021 6120PCS不用补回，剩余286pcs正常下单，PCB不下单',
        #   '2021-01-13 15:23:14', '冯瑞霞', '易子弦', 'EL.MT6683-A75(72-79V/300MA,C001,哥伦比亚,认证管控)', '601ELMT6683A75001L',
        #   'AC 100-240V/50/60HZ 宽电压输入安卓三合一板卡，50W高压(BYQ-255),背光参数72-79V/300MA,2路2pin 2.0立式背光接口并联,软件控制电流,主芯片MSD6683BQHA-8-00ED(带DD,RAM 512M),外置DDR3 256M,EMMC 4G,ATV制式：NTSC,DTV制式：DVB-T2,30PIN 2.0mm LVDS插针型屏接口(空第6PIN),驱屏电压12V,支持14PIN 2.0mm按键板接口,支持4PIN 2.54mm喇叭接口,功放供电电压12V,支持7PIN 1.25mm WIFI接口,支持2PIN 2.0mm 12V电源接口,1路RJ45网络输入,3路HDMI输入,1路AV输入（RCA）,1路RF输入(螺纹头),2路USB2.0输入,1路光纤输出,1路耳机输出,（C001,哥伦比亚）',
        #   6406.0, 'TV电源项目经理', '1741879'], ['H086',
        #                                    'SO210112023+2270V1.1_1280X800单8_20190904FJ+功放-赛维克-20200814.bin;SO210112023+2270V1.1_1280X800单8_20190904FJ+功放-赛维克-20200814.pdf',
        #                                    'SO210112023', '客户专用板\n挪芯片：SO210105018，US052270640L/3500PCS不用补回',
        #                                    '2021-01-12 19:43:11', '吴波平', '彭俊', '2270V1.1-A(AI)', '6012270V11A000002L',
        #                                    'LVDS,内置12V电源,内置VGA,支持12V,5V,3.3V屏,DC调光,功放2*2W（无头有功放）,普通板', 3500.0,
        #                                    'TV硬件项目经理', '1741795'],
        #  ['G027', 'SO210112022+鼎科技术确认书_CP4-QR-008_B3  p75-368V6.5-A  5L G027(5).pdf', 'SO210112022',
        #   '不带DD\nUS329255A00L芯片挪用SO200825038备货10000PCS不用补回', '2021-01-12 19:21:07', '吴波平', '沈维民',
        #   'P75-368V6.5-A(30-95V/700mAmax/45Wmax,G027)', '601P75368V65A0005L',
        #   '宽电压输入一体板,75W高压(EQ26P075-012110TA),背光输出30-95V/700mAmax/45Wmax(具体按照技术确认书背光参数测试老化),软件控制电流,2路并联2pin2.0背光接口,MT9255ABAN/AAZA芯片,内置512M DDR，不带DD，4GB Emmc,标准 29Pin2.0mm LVDS 屏接口,12V 驱屏电压,1 路耳机输出,2 路 3RCA 型 AV 输入,2 路 HDMI 输入(HDMI1支持UART,HDMI2支持ARC),1 路 RJ45 网口输入,2路USB2.0(单层)输入,1路同轴输出,1T1R Wifi COB,通用14Pin2.0mm按键板接口,支持PAL制ATV,DTMB标准DTV,IEC 型 RF 头,4Pin2.54mm喇叭接口,2*8W@8ohm(12V)功放,(广州柜台,G027）',
        #   10000.0, 'TV电源项目经理', '1741409'], ['C065', 'SO210112018技术确认书.pdf;SO210112018标签.pdf', 'SO210112018',
        #                                     '芯片带DD，我司购买转客户授权  \n主芯片US05663SW00L挪SO200903005   2208pcs不用补回\n技术确认SO191028022',
        #                                     '2021-01-12 20:44:17', '陈帅', '刘博鹏',
        #                                     'P75-3663SV6.0-A(39-49V/600MA,C065,认证管控）', '601P753663SV60A27L',
        #                                     '宽电压输入亚太市场一体板,75W高压(P75-1219-T1),背光输出39-49V/600MA,1路3Pin2.0mm带卡扣背光接口,硬件控制电流,MSD3663LSA-SW芯片（芯片带DD）,支持图文件丽音,PAL/SECAM标准ATV,DVB-C/T/T2标准的DTV,34Pin 2.0mm(空第6PIN)插针型屏接口,6pin控制板接口,3路HDMI输入,2路USB,1路RCA型 AVIN输入,1路光纤输出,1路耳机输出,2*6W@6ohm（12V）功放+4Pin2.54mm立式喇叭插座,新西兰,C065（特殊参数：屏VCC控制电路增加D110/4148，功放输出使用60R磁珠，耳机增加C214,C217,C221,C227/22UF，R256,R258改为10R）',
        #                                     2208.0, 'TV硬件项目经理', '1741053'],
        #  ['C065', 'SO200307001+C065技术确认书+(1).pdf;SO210112017标签.pdf', 'SO210112017',
        #   '芯片带DD，我司购买转客户授权  \n主芯片US05663SW00L挪SO200903005   1821pcs不用补回\n技术确认SO200307001', '2021-01-12 20:54:19', '陈帅',
        #   '刘博鹏', 'P75-3663SV6.0-A(57-66.5V/590MA,C065,认证管控）', '601P753663SV60A28L',
        #   '宽电压输入亚太市场一体板,75W高压(P75-1224-T1A),背光输出57-66.5V/590MA,1路3Pin2.0mm带卡扣背光接口,硬件控制电流,MSD3663LSA-SW芯片（芯片带DD）,支持图文件丽音,PAL/SECAM标准ATV,DVB-C/T/T2标准的DTV,34Pin 2.0mm(空第6PIN)插针型屏接口,6pin控制板接口,3路HDMI输入,2路USB,1路RCA型 AVIN输入,1路光纤输出,1路耳机输出,2*6W@6ohm（12V）功放+4Pin2.54mm立式喇叭插座,新西兰,C065（特殊参数：屏VCC控制电路增加D110/4148，功放输出使用60R磁珠，耳机增加C214,C217,C221,C227/22UF，R256,R258改为10R）',
        #   1821.0, 'TV硬件项目经理', '1741049'], ['C058', 'C058技术确认书+628+7L.pdf;SO210112016标签.pdf', 'SO210112016',
        #                                    '主芯片客供，USESMH6000L挪SO191115012 618PCS不用补回，技术确认书同SO201113017',
        #                                    '2021-01-12 20:17:55', '陈帅', '刘博鹏', 'P75-628MV8.0-A(63-75.6V/590mA,C058)',
        #                                    '601P75628MV80A007L',
        #                                    '宽电压输入一体板,75W低压（P75-1236-T1）,LED背光输出63-75.6V/590mA,2路3PIN2.0并联背光接口（带卡扣）,DC调光接口,MSD6A628VXM-ST（C058客户供）,内置DDR,4G EMMC ,外置512M flash,DVB-T+NTSC高频头模块,支持8位双LVDS+3D功能,12V屏电压,30Pin2.0mm盒式座子屏接口,6PIN按键板接口,5PIN IR接口,1路RJ45网口,3路HDMI输入接口（HDMI2&ARC, HDMI3&MHL）,1路VGA输入接口,1路PC-audio输入接口, 1路MINI YPBPR输入绿色接口(CVBS与YPBPR的Y共用),1路mini YPBPR/CVBS-LR声音输入接口,2路USB2.0输入接口,1路USB3.0接口,1路内置3PIN SPDIF座子输出,1路Mini 耳机输出,4PIN外置WIFI功能,2*8W@8ohm(12V)功放+2*2Pin 2.54mm喇叭插座,（台湾,C058）',
        #                                    618.0, 'TV电源硬件', '1740904']]
        # [['bs08', 'linda', 'tongfan'], ['bs08', 'linda', 'tongfan'], ['bs09', 'bill', 'liujie'],
        #  ['bs09', 'bill', 'tongfan'], ['bs01', 'linda', 'huangrenwang'], ['bs01', 'linda', 'huangrenwang'],
        #  ['bs01', 'linda']]

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

        # 获取合并当前订单数据
        Col = ['客户代码','附件名称','SO号','业务备注','制单时间','制单人员','业务员','成品名称','成品料号','成品规格','订单数量','当前步骤','PID']
        for i in range(np.array(backlist).shape[1]):
            Col.append("退回人员" + str(i+1))
        merge_data = self.merge_list(list,backlist,aix=1)
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
                            pass
                    else:                               # 无新增退回人员
                        initdata = initdata.append(saveData, ignore_index=True)  # ignore_index=True,表示不按原来的索引，从0开始自动递增
                        pd.DataFrame(initdata).to_excel(fileName, index=False)

    def merge_list(self,list1,list2,aix):
        A = np.array(list1)
        B = np.array(list2)
        if A.shape[0] == B.shape[0] and aix == 1:                # 如果两者行数相等
            C = np.hstack(A,B)
            return C
        elif A.shape[1] == B.shape[1] and aix == 0:
            C = np.vstack(A,B)
            return C
        else:
            print('合并的两个数列维度行列不能对应上')

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

    data_a = {'state': [1, 1, 2], 'pop': ['a', 'b', 'c']}
    data_b = {'state': [1, 2, 3], 'pop': ['b', 'c', 'd'],'C':['AAAA','AAAAA']}
    a = pd.DataFrame(data_a)
    b = pd.DataFrame(data_b)
    print(a.append(b))

