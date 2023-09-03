import cv2 as cv
import numpy as np


blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)

blank[200:300, 300:400] = 0,0,255
cv.imshow('red', blank)

cv.rectangle(blank,(0,0),(255,255),(255,0,0), thickness=2)
cv.imshow('rectanglle', blank)

cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=-1)
cv.imshow('circle', blank)

cv.line(blank,(100,250),(300,400),(255,255,255), thickness=3)
cv.imshow('line', blank)

cv.putText(blank,'sammakka sarrakka', (0,255), cv.FONT_HERSHEY_TRIPLEX, 1.0,(0,255,0),2)
cv.imshow('text', blank)

cv.waitKey(0)

