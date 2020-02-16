项目功能描述：
一、使用Python Web爬虫（Request库），从RDM服务器中下载待审核SO的信息（SO号，成品料号，机型，成品规格描述）以及对应技术确认书（png）
二、使用Python opencv 库进行图像分析，输出分析结果
    1、图像校正-----将技术确认书摆正
    2、形态学提取表格横线和竖线，合成获得表格边框，查找轮廓，并根据面积剔除其他轮廓，最终获得表格轮廓，根据形态学拟合4边形，获得表格四个顶点，根据四个顶点进行图像映射，完成图像矫正
    3、形态学提取表格横线和竖线，与运算，获得表格交叉点，使用矩形函数获得表格矩形坐标
    
三、成品规格描述分析
四、对比两个分析结果，将分析结果显示出来
