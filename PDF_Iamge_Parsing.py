import cv2 as cv
import numpy as np
#注意：1、文件名以及路径不能存在中文字符
Image_Path = "D:\RDM_Download\PDF_Image\SO191223070.png"
img = cv.imread(Image_Path,1)
Srcimg = img
# 加载图片，并设置为img
#人为旋转图片，方便测试纠正功能
imgInfo = img.shape
imgH = imgInfo[0]
imgW = imgInfo[1]
#旋转矩阵获取   参数1   图片中心点，参数2  旋转角度  ， 缩放系数
matRotate = cv.getRotationMatrix2D((imgH*0.5,imgW*0.5),300,0.4)
imgRotate = cv.warpAffine(img,matRotate,(imgH,imgW))
img = imgRotate
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)                       # 彩色图片转化为灰度图片
'''
自适应阈值二值化函数cv2.adaptiveThreshold(src, maxval, thresh_type, type, Block Size, C)
src          :  输入图，只能输入灰度图
maxval       :  当像素超过阈值（或者小于阈值，根据type定）
thresh_type  :  阈值计算方法， 包含以下2种类型：cv2.ADAPTIVE_THRESH_MEAN_C； cv2.ADAPTIVE_THRESH_GAUSSIAN_C
type         :  二值化操作的类型，包含以下5种类型：cv2.THRESH_BINARY,cv2.THRESH_BINARY_INV,cv2.THRESH_TRUNC,cv2.THRESH_TOZERO,cv2.THRESH_TOZERO_INV
Block Size   :  图片中分块的大小
C            :  阈值计算方法中的常数项
'''
#binary = cv.adaptiveThreshold(gray,255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
ret,binary = cv.threshold(gray,200,255,cv.THRESH_BINARY)
edge = cv.Canny(gray, 100, 120, 3)                                # 边缘检测
imgMed = cv.medianBlur(edge, 1)                                 # 去除椒盐噪声
binary = cv.GaussianBlur(imgMed,(3,3),1)                            # 高斯模糊

#cv.imshow('img', imgMed)
'''
图像轮廓检测函数cv2.findContours(image, mode, method[, contours[, hierarchy[, offset ]]])
参数：
    image:  输入图像，只能是二值图即为黑白
    mode:  
        cv2.RETR_EXTERNAL   表示只检测外轮廓
        cv2.RETR_LIST       检测的轮廓不建立等级关系
        cv2.RETR_CCOMP      建立两个等级的轮廓，上面的一层为外边界，里面的一层为内孔的边界信息。如果内孔内还有一个连通物体，这个物体的边界也在顶层。
        cv2.RETR_TREE       建立一个等级树结构的轮廓
    method:
        cv2.CHAIN_APPROX_NONE       存储所有的轮廓点，相邻的两个点的像素位置差不超过1，即max（abs（x1-x2），abs（y2-y1））==1
        cv2.CHAIN_APPROX_SIMPLE     压缩水平方向，垂直方向，对角线方向的元素，只保留该方向的终点坐标，例如一个矩形轮廓只需4个点来保存轮廓信息
        cv2.CHAIN_APPROX_TC89_L1，CV_CHAIN_APPROX_TC89_KCOS使用teh-Chinl chain 近似算法
返回值：
    contour   ： 轮廓本身，例如：图中找2个轮廓，存在contour[0],contour[1]，每一个轮廓是一个ndarray,每个ndarray是轮廓上点的集合
                 例如找一个四边形轮廓，len（contours[x]） = 4
                 可通过cv2.drawContours(img,contours,i,(0,0,255),3)进行轮廓绘制；（0，0，255）表示（b，g，r）
    
    hierarchy : ndarray，其中的元素个数和轮廓个数相同，每个轮廓contours[i]对应4个hierarchy元素
                hierarchy[i][0] ~hierarchy[i][3]，分别表示后一个轮廓、前一个轮廓、父轮廓、内嵌轮廓的索引编号，如果没有对应项，则该值为负数。

图像轮廓绘制函数cv2.drawContours(image, contours, contourIdx, color[, thickness[, lineType[, hierarchy[, maxLevel[, offset ]]]]])
image : 指明在哪一幅图上进行绘制轮廓
contours : 轮廓本身
contourIdx ：第几个轮廓，-1表示所有轮廓
'''
contours, hierarchy = cv.findContours(binary,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)         #找到图像外轮廓，并将所有点保存
outline = contours[0]
'''
多边形拟合函数approxPolyDP(InputArray curve,double epsilon,bool closed)
InputArray curve ： 输入矩阵
double epsilon   ： 精度，比如矩形只有4个点
bool closed      ： 多边形是否闭合
'''
outline = cv.approxPolyDP(outline, 4, True)
cv.polylines(img, [outline], True, (0, 255, 0), 2)
outline.shape = 4,2
if outline[0][0] != outline[1][0] :         #图片呈现一定角度倾斜
    data = np.zeros((4,2),dtype = np.int)
    DotR1 = (outline[1][0] - outline[0][0])*(outline[1][0] - outline[0][0]) + (outline[1][1] - outline[0][1])*(outline[1][1] - outline[0][1])
    DorR2 = (outline[2][0] - outline[1][0])*(outline[2][0] - outline[1][0]) + (outline[2][1] - outline[1][1])*(outline[2][1] - outline[1][1])
    if DotR1 < DorR2 :
        data[0] = outline[1]
        data[1] = outline[2]
        data[2] = outline[0]
        data[3] = outline[3]
        outline = data
    else:
        data[0] = outline[0]
        data[1] = outline[1]
        data[2] = outline[3]
        data[3] = outline[2]
        outline = data
cv.imshow('iii',img)
#cv.drawContours(img,contours,0,(0,0,255),3)
#找到文档，矩阵四个点，图像仿射变换，纠正图片
#左上角    左下角   右上角    右下角
#matsrc = np.float32([[217,335],[458,571],[384,164],[624,400]])
matsrc = np.float32(outline)
matdst = np.float32([[0,0],[0,imgH-1],[imgW-1,0],[imgW-1,imgH-1]])
matAffine = cv.getPerspectiveTransform(matsrc,matdst)
dstImg = cv.warpPerspective(img,matAffine,(imgW,imgH))
cv.imshow('img', dstImg)
cv.waitKey(0)
