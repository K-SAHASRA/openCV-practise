

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

def translate(img,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img,transMat, dimensions)
#  -x means left
#  +x means right
#  -y means up
#  +y means down

translated = translate(img, -100, 100)
cv.imshow('trans', translated )


def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width // 2, height // 2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

# IF U want to rotate clockwise then mention -ve angle if u want to rotate anticlockwise mention +ve angles

rotated = rotate(img, -45)
cv.imshow('Rotated', rotated)

rotated_rotated= rotate(rotated, -45)
cv.imshow('Rotated', rotated_rotated)
# here we wont be rotating it by 90 because the black triangles which appears when there
# there is no image is also rotated 45 degress thats why it gives this obscure image


flip = cv.flip(img,-1 )
# here 0 means flipping vertically
# 1 means flipping horizontaly
# -1 means flipping horizontaly and vertically

cv.imshow('flip',flip)




cv.waitKey(0)