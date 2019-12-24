import cv2 as cv
#注意：1、文件名以及路径不能存在中文字符
Image_Path = "D:\RDM_Download\PDF_Image\SO191206012.png"
img = cv.imread(Image_Path,1)                                    # 加载彩色图片，并设置为img
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)                 # 新建‘input image’窗口
cv.imshow("input image",img)                                     # 在‘input image’窗口内显示img
cv.waitKey(0)                                                    # 等待其他操作
cv.destroyAllWindows()