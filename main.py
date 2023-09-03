import cv2 as cv

# img = cv.imread('photos/flower.jpg')
# cv.imshow('flower', img)

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    dimensions = (width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)



#
# cv.waitKey(0)
# keyboard binding function

# def changeRes(width,height):
#     capture.set(3,width)
#     capture.set(3,height)

capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()
    frame_Resized = rescaleFrame(frame,scale=.2)
    cv.imshow('vedio', frame)
    cv.imshow('vedio resized', frame_Resized)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()

# to change the resolution of a live vedio

