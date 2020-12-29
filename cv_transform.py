import cv2 as cv
import numpy as np

src=np.array([[0,0],[200,0],[0,200]],np.float32)
print(src.shape)
dst=np.array([[0,0],[100,0],[0,100]],np.float32)
a=cv.getAffineTransform(src,dst)
print("a=",a)
print("The shape of src is",src.shape)
print("The shape of dst is",dst.shape)
print("The shape of a is",a.shape)
b=cv.getRotationMatrix2D((40,50),30,0.5)
print("The rotation matrix is",b)

if __name__=="__main__":
    image=cv.imread("/Users/admin/Desktop/CL/Python/data/img.jpg")
    #原图的高、宽
    h,w=image.shape[:2]
    #缩小2倍
    A1=np.array([[0.5,0,0],[0,0.5,0]],np.float32)
    d1=cv.warpAffine(image,A1,(w,h),borderValue=125)
    #缩小2倍，再平移
    A2=np.array([[0.5,0,w/4],[0,0.5,h/4]],np.float32)
    d2=cv.warpAffine(image,A2,(w,h),borderValue=125)
    #在d2基础上，绕图像中心点逆时针旋转30度
    A3=cv.getRotationMatrix2D((w/2.0,h/2.0),30,1)
    d3=cv.warpAffine(image,A3,(w,h),borderValue=125)
    #rotate函数
    rimg=cv.rotate(image,cv.ROTATE_90_CLOCKWISE)#顺时针旋转90度
    cv.imshow("image",image)
    cv.imshow("d1",d1)
    cv.imshow("d2",d2)
    cv.imshow("d3",d3)
    cv.imshow("rimg",rimg)
    cv.waitKey(0)
    cv.destroyAllWindows()
