import requests
import re

class Bom_Spec_Compare():
    def __init__(self,old:str,new:str):
        self.oldSpec = old
        self.newSpec = new

        self.formatSpec()
        self.comparing()

    def formatSpec(self):
        # 字符串处理函数
        # 删除多余空格
        self.oldSpec = self.oldSpec.replace(' ','')
        self.newSpec = self.newSpec.replace(' ', '')
        self.oldSpec = re.sub(r'，',',',self.oldSpec)
        self.newSpec = re.sub(r'，',',',self.newSpec)

        oldSpec_list = self.oldSpec.split(',')
        for i,data in enumerate(oldSpec_list):
            if '（' in data or '(' in data:
                if ')' in data or '）' in data:                 # 如果是xxx(xxx),一样在后面加换行符
                    oldSpec_list[i] = str(data) + '\n'
            else:
                oldSpec_list[i] = str(data) + '\n'
        self.oldSpec = ''.join(oldSpec_list)

        newSpec_list = self.newSpec.split(',')
        for i,data in enumerate(newSpec_list):
            if '（' in data or '(' in data:
                if ')' in data or '）' in data:                 # 如果是xxx(xxx),一样在后面加换行符
                    newSpec_list[i] = str(data) + '\n'
            else:
                newSpec_list[i] = str(data) + '\n'
        self.newSpec = ''.join(newSpec_list)

        print(self.oldSpec,self.newSpec)


    def comparing(self):
        # 方案一：使用differ比对（比对结果通过'+','-','?'呈现，不够直观） ------ 只能比对英文
        # # 创建differ（）对象
        # d = difflib.Differ()
        # compareResult = d.compare(oldSpec,newSpec)
        # 方案二：生成HTML文档格式的比对结果  -----  只能比对英文
        # compareResult = difflib.HtmlDiff().make_file(self.oldSpec, self.newSpec)
        # with open('diff.html', 'w+') as f:
        #     f.write(compareResult)
        pass


if __name__ == '__main__':
    # 定义oldSpec
    oldSpec = '100-240V AC交流输入一体板,P55-1224-T1,背光最大输出功率25W,背光电流700mAmax,电压范围45~65V(老化参数:65V/360mA),2PIN2.0mm并联背光接口,OB3353软件调光,TSUMV53RUUL-Z1芯片,32M DDR,不带DD,4M Flash,PAL标准ATV(单IEC头 + Tuner芯片R842),30pin2.0mm屏接口,14pin2.0mm按键板接口,1路耳机,2路USB2.0输入,2路AV IN,1路VGA + PC Audio输入,2路HDMI输入,1路COAXIAL输出,2*5W@8ohm功放'
    # 定义newSpec
    newSpec = '100-240V AC交流输入一体板,P55-1236-T1,背光最大输出功率25W,背光参数72-79V/300mA,一路2PIN2.0mm背光接口,OB3353软件调光,TSUMV53RUUL-Z1芯片,32M DDR,4M Flash,不带DD,支持PAL/SECAM/NTSC标准ATV(单IEC头,tuner芯片R842),30pin2.0mm屏接口,14pin2.0mm按键板接口,1路耳机,2路USB2.0输入,1路AV IN, 1路YPBPR,1路VGA + PC Audio输入,2路HDMI输入,1路COAXIAL输出,2*8W@8ohm功放(沙特阿拉伯,C001)'

    compare = Bom_Spec_Compare(oldSpec,newSpec)