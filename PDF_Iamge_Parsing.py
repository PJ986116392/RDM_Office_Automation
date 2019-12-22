import cv2 as cv
#注意：1、文件名以及路径不能存在中文字符
Image_Path = "D:\RDM_Download\PDF_Image\SO191206012.png"
img = cv.imread(Image_Path,1)
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",img)
cv.waitKey(0)
cv.destroyAllWindows()