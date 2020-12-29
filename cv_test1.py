#导入cv模块
import cv2 as cv
import numpy as np

z=np.zeros((2,4),np.uint8)
print("The type of z is:",type(z))
print("z:",z)
o=np.ones((2,4),np.int32)
print("o:",o)
m=np.array([[4,12,3,1],[10,12,14,29]],np.float32)
print(m)
m=np.array(
    [
        [[1,2,3,4],[5,6,7,8]],
        [[10,11,12,14],[15,16,17,18]]
    ],np.float32
)
print(m)

print("-------------------------------------")
a=np.array([[1,2,3],[4,5,6]])
b=np.array([[7,8,9],[10,11,12]])
print("a+b=",a+b)
c=cv.add(a,b)
print(c)
print("a*b=",a*b)# 对应元素相乘
print("a*b=",np.multiply(a,b))
print("a/b=",a/b)
d=np.array([[1,2],[3,4],[5,6]])
print(np.dot(c,d))
print(np.power(a,2))

#读取图像，支持 bmp、jpg、png、tiff 等常用格式
img = cv.imread("/Users/admin/Desktop/CL/Python/data/color.jpeg",cv.IMREAD_ANYCOLOR)
print(img.shape)
# 创建窗口并显示图像
cv.namedWindow("Image")
cv.imshow("Image",img)
# cv.waitKey(0)
# 释放窗口
# cv2.destroyAllWindows()
#得到三通道
b=img[:,:,0]
g=img[:,:,1]
r=img[:,:,2]
cv.imshow("b",b)
cv.imshow("g",g)
cv.imshow("r",r)
cv.waitKey(0)
cv.destroyAllWindows()
