import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img = cv.imread('photos/flower.jpg')
# cv.imshow('flower', img)
def rescaleFrame(img, scale=0.25):
    width = int(img.shape[1]*scale)
    height = int(img.shape[0]*scale)

    dimensions = (width,height)
    return cv.resize(img,dimensions,interpolation=cv.INTER_AREA)

img = rescaleFrame(img,0.25)
cv.imshow('small img',img)


# wwe can specify what colour space we want to convert to byspecifying the colour code
# cv.COLOR_BGR(THE NORMAL IMAGE FORMAT )2GRAY/HSV(THE FORMAT WE WANT TO CONVERT TO )
# cv.COLOR_BGR2GRAY
#
# plt.imshow(img)
# plt.show()
# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

# HSV to BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('LAB --> BGR', lab_bgr)

# you cannot direcrtlt convert to different color spaces u have to convert back to bgr and then to the next

cv.waitKey(0)