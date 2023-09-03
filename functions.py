
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


gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('blur', blur)
# to increas ethe blur increase the kernal size

canny = cv.Canny(img,125,175)
cv.imshow('canny',canny)

dilated = cv.dilate(canny, (7,7), iterations=1)
cv.imshow('dilate',dilated)

eroded = cv.erode(dilated,(7,7), iterations=1)
cv.imshow('erode',eroded)


resized = cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('resized',resized)

cropped = img[50:200, 200:400]
cv.imshow('crop',cropped)



cv.waitKey(0)

