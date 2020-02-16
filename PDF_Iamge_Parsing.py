import cv2
import numpy as np
import math
from imutils.perspective import four_point_transform
import imutils

def FindContours(AdaptiveThreshold,ExternalContours):

    horizontal = AdaptiveThreshold.copy()
    vertical = AdaptiveThreshold.copy()
    scale = 20

    horizontalSize = int(horizontal.shape[1]/scale)
    horizontalStructure = cv2.getStructuringElement(cv2.MORPH_RECT, (horizontalSize, 1))
    horizontal = cv2.erode(horizontal, horizontalStructure)                              #腐蚀图像,黑色加强
    horizontal = cv2.dilate(horizontal, horizontalStructure)                             #膨胀图像,白色加强
    #cv2.imshow("horizontal", horizontal)
    #cv2.waitKey(0)

    verticalsize = int(vertical.shape[1]/scale)

    verticalStructure = cv2.getStructuringElement(cv2.MORPH_RECT, (1, verticalsize))
    vertical = cv2.erode(vertical, verticalStructure, (-1, -1))                          #腐蚀图像,黑色加强
    vertical = cv2.dilate(vertical, verticalStructure, (-1, -1))                         #膨胀图像,白色加强
    #cv2.imshow("verticalsize", vertical)
    #cv2.waitKey(0)

    mask = horizontal + vertical
    #cv2.imshow("mask", mask)
    #cv2.waitKey(0)

    Net_img = cv2.bitwise_and(horizontal, vertical)
    #cv2.imshow("Net_img", Net_img)
    #cv2.waitKey(0)
    cv2.destroyAllWindows()
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
    '''
    if ExternalContours == True :
        contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    else:
        contours, hierarchy = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    '''
    图像轮廓绘制函数cv2.drawContours(image, contours, contourIdx, color[, thickness[, lineType[, hierarchy[, maxLevel[, offset ]]]]])
    image : 指明在哪一幅图上进行绘制轮廓
    contours : 轮廓本身
    contourIdx ：第几个轮廓，-1表示所有轮廓
    '''
    #=========================绘出所有轮廓=========================
    #IMG = cv2.drawContours(src_img0, contours, -1, (0, 255, 255), 1)
    #cv2.imshow('IMG' , IMG)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    #=============================================================
    return Net_img,contours

def get_Affine_Location(src_img,contours):
    contours = sorted(contours, key=cv2.contourArea, reverse=True)          #根据闭合图形面积大小重新排序，根据面积进行降序
    for cnt in contours:
        area0 = cv2.contourArea(cnt)
        if area0<10000:continue
        '''
        #取最上的一个点
        topmost = cnt[cnt[:, :, 1].argmin()][0]
        while True:
            bottommost = cnt[cnt[:, :, 1].argmax()][0]
            r1 = np.linalg.norm(topmost-bottommost)
            if r1 < 300 : cnt = np.delete(cnt, cnt[:, :, 1].argmax(), axis = 0)
            else : break

        while True:
            leftmost = cnt[cnt[:, :, 0].argmin()][0]
            r1 = np.linalg.norm(topmost-leftmost)
            r2 = np.linalg.norm(bottommost-leftmost)
            if r1 < 300 or r2 < 300 : cnt = np.delete(cnt, cnt[:, :, 0].argmin(), axis = 0)
            else: break

        while True:
            rightmost = cnt[cnt[:, :, 0].argmax()][0]
            r1 = np.linalg.norm(topmost - rightmost)
            r2 = np.linalg.norm(bottommost - rightmost)
            r3 = np.linalg.norm(leftmost - rightmost)
            if r1 < 300 or r2 < 300 or r3 < 300 : cnt = np.delete(cnt, cnt[:, :, 0].argmax(), axis = 0)
            else:break

        topmost = tuple(topmost)
        bottommost = tuple(bottommost)
        leftmost = tuple(leftmost)
        rightmost = tuple(rightmost)

        print(leftmost,rightmost,topmost,bottommost)

        cv2.circle(src_img, topmost, 5, (0, 255, 0), 1)
        cv2.circle(src_img, bottommost, 5, (0, 255, 0), 1)
        cv2.circle(src_img, leftmost, 5, (0, 255, 0), 1)
        cv2.circle(src_img, rightmost, 5, (0, 255, 0), 1)
    
        cv2.namedWindow('ss', cv2.WINDOW_NORMAL)
        cv2.imshow('ss', src_img)
        cv2.waitKey(0)
        '''
        # =======================查找每个表的关节数====================
        epsilon = 0.1 * cv2.arcLength(cnt, True)
        '''
        多边形拟合函数approxPolyDP(InputArray curve,double epsilon,bool closed)
        InputArray curve ： 输入矩阵
        double epsilon   ： 精度，比如矩形只有4个点
        bool closed      ： 多边形是否闭合
        '''
        approx = cv2.approxPolyDP(cnt, epsilon, True)  # 获取近似轮廓

        '''
        # =======================无旋转矩形轮廓查找绘制=============================
        #boundingRect(approx)  用一个最小的矩形（无旋转），把找到的形状包起来，返回一个数组[x,y,w,h] 
        #x,y分别为矩形的第一个顶点坐标，w,h为这个矩形的宽高，与rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)函数配套使用
        x1, y1, w1, h1 = cv2.boundingRect(approx)
        roi = Net_img[int(y1):int(y1+h1) ,int(x1):int(x1+w1)]
        roi_contours, hierarchy = cv2.findContours(roi, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
        print('len(roi_contours):',len(roi_contours))
        
        #绘制查找的矩形和保存截取的图片
        #src_img1 = cv2.rectangle(src_img, (x1, y1),(x1+w1,y1+h1), (0,255,0), 2)
        #cut_img = src_img[y1:y1+h1,x1:x1+w1]
        #cv2.imwrite(cutImg_path+'/'+cutImg_name+'_'+str(i)+'.png',cut_img)      # 保存截取的图片
        #cv2.imshow('src_img_'+str(i),src_img1)
        #cv2.waitKey(0)
        
        #========================带旋转的矩形轮廓查找绘制===============================
        #cv2.minAreaRect(points)
        #计算指定点集的最小区域的边界矩形，矩形可能会发生旋转 possibly rotated，以保证区域面积最小
        #points      :    2D点的矢量
        #返回值      :    ((x, y), (w, h), θ )元组（（最小外接矩形的中心坐标），（宽，高），旋转角度）
        #但绘制这个矩形，一般需要知道矩形的 4 个顶点坐标；通常是通过函数 cv2.boxPoints()获取
        
        #rect = cv2.minAreaRect(contours[i])
        #print(rect)
        #box = cv2.boxPoints(rect)
        #box = np.int0(box)
        #cv2.drawContours(src_img, [box], 0, (0, 0, 255), 1)
        #cv2.imshow('text',src_img)
        #cv2.waitKey(0)
        '''
        # =========================绘出最大轮廓凸包并矫正图像==========================
        # epsilon = 0.1 * cv2.arcLength(contours[0], True)
        # approx = cv2.approxPolyDP(contours[0], epsilon, True)         # 获取近似轮廓
        # hull = cv2.convexHull(approx)                                 # 默认返回坐标点
        # hull_img = cv2.polylines(src_img, [hull], True, (0, 255, 0), 2)
        # cv2.imshow('hull_img', hull_img)
        # cv2.waitKey(0)
        #
        # if len(hull) == 4:
        #     dst = four_point_transform(src_img, hull.reshape(4,2))    # 矫正变换
        #     cv2.imwrite(cutImg_path+'/'+cutImg_name+'max.png', dst)   # 保存截取的图片
        #     cv2.imshow("result", dst)
        #     cv2.waitKey(0)
        #
        # Img_max = cv2.drawContours(src_img, contours, 0, (0, 255, 0), 2, 1)
        # cv2.imshow('ImgMax', Img_max)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        hull = cv2.convexHull(approx)                                 # 默认返回坐标点
        #hull_img = cv2.polylines(src_img, [hull], True, (0, 255, 0), 2)
        #cv2.namedWindow('hull_img', cv2.WINDOW_NORMAL)
        #cv2.imshow('hull_img', hull_img)
        #cv2.waitKey(0)

        if len(hull) == 4:
            dst = four_point_transform(src_img, hull.reshape(4,2))    # 矫正变换
            #cv2.imshow("result", dst)
            #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    return  dst

def Img_Roate(img_path):
    image = cv2.imread(img_path)
    rows, cols, channels = image.shape
    #print(rows, cols)
    image_copy = image.copy()

    ##### 旋转校正Rotation #####
    # 统计图中长横线的斜率来判断整体需要旋转矫正的角度
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    cv2.imshow('gray',gray)
    cv2.waitKey(0)
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)  # 50,150,3
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 200, 0, minLineLength=50, maxLineGap=35)  # 650,50,20
    '''
    if table_style == 1 or table_style == 3 or table_style == 2:
        edges = cv.Canny(gray, 50, 150, apertureSize=3)  # 50,150,3
        cv.imwrite('edges_whole.jpg', edges)
        lines = cv.HoughLinesP(edges, 1, np.pi / 180, 500, 0, minLineLength=50, maxLineGap=50)  # 650,50,20
    if table_style == 4:
        edges_gray = cv.Canny(gray, 50, 150, apertureSize=3)  # 50,150,3
        edges = edges_gray[400:1000, 0:1000]
        cv.imwrite('edges_whole.jpg', edges)
        lines = cv.HoughLinesP(edges, 1, np.pi / 180, 200, 0, minLineLength=50, maxLineGap=35)  # 650,50,20
    '''
    pi = 3.1415
    theta_total = 0
    theta_count = 0
    for line in lines:
        x1, y1, x2, y2 = line[0]
        #if table_style == 4:
        #    y1 = y1 + 400
        #    y2 = y2 + 400
        rho = np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        theta = math.atan(float(y2 - y1) / float(x2 - x1 + 0.001))
        print(rho, theta, x1, y1, x2, y2)
        if theta < pi / 4 and theta > -pi / 4:
            theta_total = theta_total + theta
            theta_count += 1
            #cv2.line(image_copy, (x1, y1), (x2, y2), (0, 0, 255), 1)
        # cv.line(edges, (x1, y1), (x2, y2), (0, 0, 0), 2)
    theta_average = theta_total / theta_count
    #print (theta_average, theta_average * 180 / pi)
    # cv.imwrite('line_detect4rotation.jpg', ~edges)
    # affineShrinkTranslationRotation = cv.getRotationMatrix2D((cols/2, rows/2), theta_average*180/pi, 1)
    affineShrinkTranslationRotation = cv2.getRotationMatrix2D((0, rows), theta_average * 180 / pi, 1)
    ShrinkTranslationRotation = cv2.warpAffine(image, affineShrinkTranslationRotation, (cols, rows))
    image = cv2.warpAffine(image_copy, affineShrinkTranslationRotation, (cols, rows))
    cv2.imshow('img',image)
    cv2.waitKey(0)
    return image

if __name__ == '__main__':
    # 文件名以及路径不能存在中文字符
    Image_Path = "D:/RDM_Download/PDF_Image/SO200115048.png"
    #cutImg_path = 'D:\\RDM_Download\\PDF_Image'
    #cutImg_name = Image_Path.split('/')[-1][:-4]

    #图片前期预处理：读取，灰阶，高斯模糊，取反，二值化
    src_img = cv2.imread(Image_Path,cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(src_img, cv2.COLOR_BGR2GRAY)
    Gauss = cv2.GaussianBlur(gray,(3,3),0)
    Gauss_Not = cv2.bitwise_not(Gauss)
    '''
    自适应阈值二值化函数cv2.adaptiveThreshold(src, maxval, thresh_type, type, Block Size, C)
    src          :  输入图，只能输入灰度图
    maxval       :  当像素超过阈值（或者小于阈值，根据type定）
    thresh_type  :  阈值计算方法， 包含以下2种类型：cv2.ADAPTIVE_THRESH_MEAN_C； cv2.ADAPTIVE_THRESH_GAUSSIAN_C
    type         :  二值化操作的类型，包含以下5种类型：cv2.THRESH_BINARY,cv2.THRESH_BINARY_INV,cv2.THRESH_TRUNC,cv2.THRESH_TOZERO,cv2.THRESH_TOZERO_INV
    Block Size   :  图片中分块的大小
    C            :  阈值计算方法中的常数项
    '''
    AdaptiveThreshold = cv2.adaptiveThreshold(Gauss_Not, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, -2)

    #图片矫正,提取最大的矩形
    Net_img,contours = FindContours(AdaptiveThreshold,True)                 #输入二值图
    dst = get_Affine_Location(src_img, contours)

    #识别表格中的矩形
    gray = cv2.cvtColor(dst,cv2.COLOR_BGR2GRAY)
    gray_not = cv2.bitwise_not(gray)
    AdaptiveThreshold = cv2.adaptiveThreshold(gray_not, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, -2)
    Net_img,contours = FindContours(AdaptiveThreshold,False)

    small_rects = []
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area < 10: continue
        approx = cv2.approxPolyDP(cnt, 4, True)  # 3
        x, y, w, h = cv2.boundingRect(approx)
        rect = (x, y, w, h)
        # cv.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
        roi = Net_img[y:y + h, x:x + w]
        joints_contours, joints_hierarchy = cv2.findContours(roi, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        # print len(joints_contours)
        # if h < 80 and h > 20 and w > 10 and len(joints_contours)<=4:
        if  h > 10 and w > 10 and len(joints_contours) <= 15:  # important
            small_rects.append(rect)

    for Rect in small_rects:
        x,y,w,h = Rect
        cv2.rectangle(dst, (x, y), (x + w, y + h), (0,0,255), 2)
        cv2.namedWindow('Net', cv2.WINDOW_NORMAL)
        cv2.imshow('Net',dst)
        cv2.waitKey(0)
    cv2.destroyAllWindows()
