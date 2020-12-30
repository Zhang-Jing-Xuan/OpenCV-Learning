import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv


def histplt(pixelSequence,numberBins):
    histogram,bins,patch=plt.hist(pixelSequence,numberBins,facecolor='black',histtype='bar')
    plt.xlabel(u"gray Label")
    plt.ylabel(u"number of pixels")
    y_maxValue=np.max(histogram)
    plt.axis([0,255,0,y_maxValue])
    plt.show()

if __name__=="__main__":
    image=cv.imread("/Users/admin/Desktop/CL/Python/data/img3.jpg")
    rows,cols=image.shape[:2]
    pixelSequence=image.reshape([rows*cols,-1])
    numberBins=256
    histplt(pixelSequence,numberBins)
    #线性变换
    a=2
    Output=float(a)*image
    Output[Output>255]=255
    Output=np.round(Output)
    Output=Output.astype(np.uint8)
    cv.imshow("image",image)
    cv.imshow("Output_linear",Output)
    #正规化
    Imax=np.max(image)
    Imin=np.min(image)
    Omin,Omax=0,255
    a=(float)(Omax-Omin)/(Imax-Imin)
    b=Omin-a*Imin
    Output=a*image+b
    Output=Output.astype(np.uint8)
    cv.imshow("image",image)
    cv.imshow("Output_normalization",Output)

    cv.waitKey(0)
    cv.destroyAllWindows()
