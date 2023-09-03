import cv2 as cv

img = cv.imread('photos/flower.jpg')
# cv.imshow('flower', img)

def rescaleFrame(img, scale=0.25):
    width = int(img.shape[1]*scale)
    height = int(img.shape[0]*scale)

    dimensions = (width,height)
    return cv.resize(img,dimensions,interpolation=cv.INTER_AREA)

img = rescaleFrame(img,0.25)
cv.imshow('small img',img)

average = cv.blur(img, (3,3))
cv.imshow('average', average)

guass = cv.GaussianBlur(img, (3,3),0)
cv.imshow('gauss', guass)

median = cv.medianBlur(img, 3)
cv.imshow('median', median)

bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('bilateral', bilateral)

cv.waitKey(0)