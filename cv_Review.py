import cv2 as cv#BGR格式
import matplotlib.pyplot as plt
import numpy as np
import os

os.chdir("/Users/admin/Desktop/CL/Python/OpenCV")

def cv_show(name,img):
    cv.imshow(name,img)
    cv.waitKey(0)
    cv.destroyAllWindows()
# cv_show("img",cv.imread("img4.jpg"))
# print(img.shape)
# print(img.dtype)#uint8
# print(img.size)#134268
# print(type(img))#<class 'numpy.ndarray'>

'''读取视频
vc=cv.VideoCapture("1.mov")
if vc.isOpened():
    open,frame=vc.read()
else:
    open=False
while open:
    ret,frame=vc.read()
    if frame is None:
        break
    if ret==True:
        gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        cv.imshow('result',gray)
        if cv.waitKey(10)&0xFF==27:
            break
vc.release()
cv.destroyAllWindows()
'''
img=cv.imread("img4.jpg")
p=img[50:100,0:200]
cv_show('image',p)
b,g,r=cv.split(img)
img1=cv.merge((b,g,r))
#只保留R
cur_img=img.copy()
cur_img[:,:,0]=0
cur_img[:,:,1]=0
cv_show('R',cur_img)
#边界填充
top_size,bottom_size,left_size,right_size = (50,50,50,50)
replicate = cv.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, borderType=cv.BORDER_REPLICATE)
reflect = cv.copyMakeBorder(img, top_size, bottom_size, left_size, right_size,cv.BORDER_REFLECT)
reflect101 = cv.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, cv.BORDER_REFLECT_101)
wrap = cv.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, cv.BORDER_WRAP)
constant = cv.copyMakeBorder(img, top_size, bottom_size, left_size, right_size,cv.BORDER_CONSTANT, value=0)

plt.subplot(231), plt.imshow(img, 'gray'), plt.title('ORIGINAL')
plt.subplot(232), plt.imshow(replicate, 'gray'), plt.title('REPLICATE')
plt.subplot(233), plt.imshow(reflect, 'gray'), plt.title('REFLECT')
plt.subplot(234), plt.imshow(reflect101, 'gray'), plt.title('REFLECT_101')
plt.subplot(235), plt.imshow(wrap, 'gray'), plt.title('WRAP')
plt.subplot(236), plt.imshow(constant, 'gray'), plt.title('CONSTANT')

plt.show()


