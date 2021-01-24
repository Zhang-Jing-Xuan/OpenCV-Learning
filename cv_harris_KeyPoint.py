import cv2 
import numpy as np
import os

os.chdir("/Users/admin/Desktop/CL/Python/OpenCV")
#Harris角点检测
img = cv2.imread('img4.jpg')
print ('img.shape:',img.shape)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# gray = np.float32(gray)
dst = cv2.cornerHarris(gray, 2, 3, 0.04)
print ('dst.shape:',dst.shape)
img[dst>0.01*dst.max()]=[0,0,255]
cv2.imshow('dst',img) 
#图像关键点检测
img = cv2.imread('img4.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
sift = cv2.SIFT_create()
kp = sift.detect(gray, None)
img = cv2.drawKeypoints(gray, kp, img)
cv2.imshow('drawKeypoints', img)
cv2.waitKey(0) 
cv2.destroyAllWindows()

kp, des = sift.compute(gray, kp)
print (np.array(kp).shape)
print(des.shape)
print(des[0])