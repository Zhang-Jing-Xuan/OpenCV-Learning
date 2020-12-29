import cv2 as cv
import numpy as np
src=np.array([[0,0],[200,0],[0,200]],np.float32)
print(src.shape)
dst=np.array([[0,0],[100,0],[0,100]],np.float32)
a=cv.getAffineTransform(src,dst)
print(a)
print(src.shape)
print(dst.shape)
print(a.shape)