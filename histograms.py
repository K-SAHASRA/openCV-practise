import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
img = cv.imread('photos/flower.jpg')
# cv.imshow('flower', img)

def rescaleFrame(img, scale=0.25):
    width = int(img.shape[1]*scale)
    height = int(img.shape[0]*scale)

    dimensions = (width,height)
    return cv.resize(img,dimensions,interpolation=cv.INTER_AREA)

img = rescaleFrame(img,0.25)
cv.imshow('small img',img)

blank = np.zeros(img.shape[:2], dtype='uint8')


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)


mask = cv.circle(blank, (img.shape[1]//2+45, img.shape[0]//2),100,255,-1)
masked = cv.bitwise_and(img,img,mask=mask)
cv.imshow('mask', masked)

gray_hist = cv.calcHist([gray], [ 0], None,[256], [0,256])

plt.figure()
plt.title('grayscale histogram')
plt.xlabel('bins')
plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

colors = ('b','g','r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img],[i], None, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])

plt.show()


cv.waitKey(0)