import os
import numpy as np
import cv2
import matplotlib.pyplot as plt

os.chdir("/Users/admin/Desktop/CL/Python/OpenCV")
# img=cv2.imread("img4.jpg")
# cv2.imshow("img",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
def cv_show(img,name):
    cv2.imshow(name,img)
    cv2.waitKey()
    cv2.destroyAllWindows()
#Sobel算子
img=cv2.imread("img4.jpg")
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)
cv_show(sobelx,'sobelx')
#白到黑是正数，黑到白就是负数了，所有的负数会被截断成0，所以要取绝对值
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)
sobelx = cv2.convertScaleAbs(sobelx)
cv_show(sobelx,'sobelx')
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=3)
sobely = cv2.convertScaleAbs(sobely)  
cv_show(sobely,'sobely')
#分别计算x和y，再求和分别计算x和y，再求和
sobelxy = cv2.addWeighted(sobelx,0.5,sobely,0.5,0)
cv_show(sobelxy,'sobelxy')
#各种算子的对比
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=3)
sobelx = cv2.convertScaleAbs(sobelx)   
sobely = cv2.convertScaleAbs(sobely)  
sobelxy =  cv2.addWeighted(sobelx,0.5,sobely,0.5,0)  

scharrx = cv2.Scharr(img,cv2.CV_64F,1,0)
scharry = cv2.Scharr(img,cv2.CV_64F,0,1)
scharrx = cv2.convertScaleAbs(scharrx)   
scharry = cv2.convertScaleAbs(scharry)  
scharrxy =  cv2.addWeighted(scharrx,0.5,scharry,0.5,0) 

laplacian = cv2.Laplacian(img,cv2.CV_64F)
laplacian = cv2.convertScaleAbs(laplacian)   

res = np.hstack((sobelxy,scharrxy,laplacian))
cv_show(res,'res')
'''
Canny边缘检测
1) 使用高斯滤波器，以平滑图像，滤除噪声。

2) 计算图像中每个像素点的梯度强度和方向。

3) 应用非极大值（Non-Maximum Suppression）抑制，以消除边缘检测带来的杂散响应。

4) 应用双阈值（Double-Threshold）检测来确定真实的和潜在的边缘。

5) 通过抑制孤立的弱边缘最终完成边缘检测。
'''
v1=cv2.Canny(img,80,150)
v2=cv2.Canny(img,50,100)

res = np.hstack((v1,v2))
cv_show(res,'res')
v1=cv2.Canny(img,120,250)
v2=cv2.Canny(img,50,100)

res = np.hstack((v1,v2))
cv_show(res,'res')