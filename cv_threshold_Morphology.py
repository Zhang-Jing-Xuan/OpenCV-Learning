import os
import numpy as np
import cv2
import matplotlib.pyplot as plt

os.chdir("/Users/admin/Desktop/CL/Python/OpenCV")
img_gray=cv2.imread("img4.jpg")
img=img_gray
ret, thresh1 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)#>127->255,<127->0
ret, thresh2 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV)#>127->0,<127->255
ret, thresh3 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_TRUNC)#>127->127,<127->不变
ret, thresh4 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_TOZERO)#>127->不变,<=127->0
ret, thresh5 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_TOZERO_INV)

titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6):
    plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()

cv2.imshow('img', img)
cv2.waitKey(0)
# print(img)
# cv2.destroyAllWindows()
# 均值滤波
# 简单的平均卷积操作
blur = cv2.blur(img, (3, 3))
cv2.imshow('blur', blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
# print("blur",blur)
# 方框滤波
# 基本和均值一样，可以选择归一化
box = cv2.boxFilter(img,-1,(3,3), normalize=True)  
cv2.imshow('box1', box)
cv2.waitKey(0)
cv2.destroyAllWindows()
# 方框滤波
# 基本和均值一样，可以选择归一化,容易越界
box = cv2.boxFilter(img,-1,(3,3), normalize=False)  
cv2.imshow('box2', box)
cv2.waitKey(0)
cv2.destroyAllWindows()
# 高斯滤波
# 高斯模糊的卷积核里的数值是满足高斯分布，相当于更重视中间的
aussian = cv2.GaussianBlur(img, (5, 5), 1)  
cv2.imshow('aussian', aussian)
cv2.waitKey(0)
cv2.destroyAllWindows()
# 中值滤波
# 相当于用中值代替
median = cv2.medianBlur(img, 5)  # 中值滤波
cv2.imshow('median', median)
cv2.waitKey(0)
cv2.destroyAllWindows()
# 展示所有的
res = np.hstack((blur,aussian,median))#vstack
#print (res)
cv2.imshow('median vs average', res)
cv2.waitKey(0)
cv2.destroyAllWindows()
#腐蚀
kernel = np.ones((10,10),np.uint8) 
erosion_1 = cv2.erode(img,kernel,iterations = 1)
erosion_2 = cv2.erode(img,kernel,iterations = 2)
erosion_3 = cv2.erode(img,kernel,iterations = 3)
res = np.hstack((erosion_1,erosion_2,erosion_3))
cv2.imshow('res', res)
cv2.waitKey(0)
cv2.destroyAllWindows()
#膨胀
kernel = np.ones((10,10),np.uint8) 
dilate_1 = cv2.dilate(img,kernel,iterations = 1)
dilate_2 = cv2.dilate(img,kernel,iterations = 2)
dilate_3 = cv2.dilate(img,kernel,iterations = 3)
res = np.hstack((dilate_1,dilate_2,dilate_3))
cv2.imshow('res', res)
cv2.waitKey(0)
cv2.destroyAllWindows()
# 开：先腐蚀，再膨胀
kernel = np.ones((5,5),np.uint8) 
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
cv2.imshow('opening', opening)
cv2.waitKey(0)
cv2.destroyAllWindows()
# 闭：先膨胀，再腐蚀
kernel = np.ones((5,5),np.uint8) 
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
cv2.imshow('closing', closing)
cv2.waitKey(0)
cv2.destroyAllWindows()
# 梯度=膨胀-腐蚀
kernel = np.ones((7,7),np.uint8) 
dilate = cv2.dilate(img,kernel,iterations = 5)
erosion = cv2.erode(img,kernel,iterations = 5)
res = np.hstack((dilate,erosion))
cv2.imshow('res', res)
cv2.waitKey(0)
cv2.destroyAllWindows()
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
cv2.imshow('gradient', gradient)
cv2.waitKey(0)
cv2.destroyAllWindows()
#礼帽 = 原始输入-开运算结果(刺)
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
cv2.imshow('tophat', tophat)
cv2.waitKey(0)
cv2.destroyAllWindows()
#黑帽 = 闭运算-原始输入（没有刺，只有轮廓）
blackhat  = cv2.morphologyEx(img,cv2.MORPH_BLACKHAT, kernel)
cv2.imshow('blackhat ', blackhat )
cv2.waitKey(0)
cv2.destroyAllWindows()
