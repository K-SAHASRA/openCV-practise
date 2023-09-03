import cv2 as cv
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





cv.waitKey(0)