import cv2
import numpy as np 
import sys
import math 

def polar(I, center, r, theta= (0,360), rstep = 1.0, thetastep = 360.0/(180*8)):
	#得到距离最小最大的范围
	minr, maxr = r
	#得到角度最小最大范围
	mintheta, maxtheta = theta
	#
	H = int((maxr - minr) / rstep) +1
	W = int((maxtheta - mintheta) / thetastep) +1
	O = 125 * np.ones((H, W), I.dtype)
	r = np.linspace(minr,maxr,H)			
	r = np.tile(r,(W,1))
	r = np.transpose(r)
	theta = np.linspace(mintheta,maxtheta,W)
	theta = np.tile(theta,(H,1))
	x,y=cv2.polarToCart(r,theta,angleInDegrees=True)


	#最近邻插值
	for i in range(H):
		for j in range(W):
			px = int(round(x[i][j])+cx)
			py = int(round(y[i][j])+cy)
			if((px >= 0 and px <= w-1) and (py >= 0 and py <= h-1)):
				O[i][j] = I[py][px]
			else:
				O[i][j] = 125#灰色
	return O
    
#主函数
if __name__ == "__main__":
	imagePath = "/Users/admin/Desktop/CL/Python/data/img2.jpg"
	image = cv2.imread(imagePath, cv2.IMREAD_GRAYSCALE)
	
    #图像的宽高
	h,w = image.shape[:2]
	print (w,h)
    #极左标变换的中心
	cx,cy = 508,503
	print (cx,cy)
	cv2.circle(image,(int(cx),int(cy)),10,(255.0,0,0),3)
    #距离的最小最大半径 #200 550 270,340
	O = polar(image,(cx,cy),(0,550))
    #旋转
	O = cv2.flip(O,0)
    #显示原图和输出图像
	cv2.imshow("image",image)
	cv2.imshow("O",O)
	cv2.imwrite("O.jpg",O)
	cv2.waitKey(0)
	cv2.destroyAllWindows()


