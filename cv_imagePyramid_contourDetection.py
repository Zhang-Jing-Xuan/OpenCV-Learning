import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

os.chdir("/Users/admin/Desktop/CL/Python/OpenCV")
def cv_show(img,name):
    cv2.imshow(name,img)
    cv2.waitKey()
    cv2.destroyAllWindows()

img=cv2.imread("img4.jpg")
cv_show(img,"origin")
print (img.shape)
#高斯金字塔：向上采样方法（放大）
up=cv2.pyrUp(img)
cv_show(up,'up')
print (up.shape)
#高斯金字塔：向下采样方法（缩小）
down=cv2.pyrDown(img)
cv_show(down,'down')
print (down.shape)
#高斯金字塔先向上再向下
up=cv2.pyrUp(img)
up_down=cv2.pyrDown(up)
cv_show(up_down,'up_down')
cv_show(np.hstack((img,up_down)),'up_down')
up=cv2.pyrUp(img)
up_down=cv2.pyrDown(up)
cv_show(img-up_down,'img-up_down')
#第一层Laplace金字塔
down=cv2.pyrDown(img)
down_up=cv2.pyrUp(down)
l_1=img-down_up
cv_show(l_1,'l_1')
#轮廓检测
'''
cv2.findContours(img,mode,method)
mode:轮廓检索模式

RETR_EXTERNAL ：只检索最外面的轮廓；
RETR_LIST：检索所有的轮廓，并将其保存到一条链表当中；
RETR_CCOMP：检索所有的轮廓，并将他们组织为两层：顶层是各部分的外部边界，第二层是空洞的边界;
RETR_TREE：检索所有的轮廓，并重构嵌套轮廓的整个层次;（最常用）
method:轮廓逼近方法

CHAIN_APPROX_NONE：以Freeman链码的方式输出轮廓，所有其他方法输出多边形（顶点的序列）。
CHAIN_APPROX_SIMPLE:压缩水平的、垂直的和斜的部分，也就是，函数只保留他们的终点部分。
'''
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
cv_show(thresh,'thresh')
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
#传入绘制图像，轮廓，轮廓索引，颜色模式，线条厚度
# 注意需要copy,要不原图会变。。。
draw_img = img.copy()
res = cv2.drawContours(draw_img, contours, -1, (0, 0, 255), 2)
cv_show(res,'res')
draw_img = img.copy()
res = cv2.drawContours(draw_img, contours, 0, (0, 0, 255), 2)
cv_show(res,'res')
#轮廓特征
cnt = contours[0]
print("area=",cv2.contourArea(cnt))
print("Length=",cv2.arcLength(cnt,True))
#轮廓近似
img = cv2.imread('contours.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
cnt = contours[0]
draw_img = img.copy()
res = cv2.drawContours(draw_img, [cnt], -1, (0, 0, 255), 2)
cv_show(res,'res')

epsilon = 0.15*cv2.arcLength(cnt,True) 
approx = cv2.approxPolyDP(cnt,epsilon,True)
draw_img = img.copy()
res = cv2.drawContours(draw_img, [approx], -1, (0, 0, 255), 2)
cv_show(res,'res')


