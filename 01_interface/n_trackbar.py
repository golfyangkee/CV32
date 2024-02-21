import numpy as np
import cv2 as cv
def myFun(X):
        # get current positions of four trackbars
        r = cv.getTrackbarPos('R','image')
        g = cv.getTrackbarPos('G','image')
        b = cv.getTrackbarPos('B','image')
        s = cv.getTrackbarPos(switch,'image')
        if s == 0:
            img[:] = 0
        else:
            img[:] = [b,g,r]
        cv.imshow('image',img)


# Create a black image, a window
img = np.zeros((300,512,3), np.uint8)
cv.namedWindow('image')
# create trackbars for color change
cv.createTrackbar('R','image',0,255,myFun)
cv.createTrackbar('G','image',0,255,myFun)
cv.createTrackbar('B','image',0,255,myFun)
# create switch for ON/OFF functionality
switch = '0 : OFF \n1 : ON'
cv.createTrackbar(switch, 'image',0,1,myFun)

while True:
    k= cv.waitKey(1) & 0xFF
    if k == 27:     # esc로 종료
        break

cv.destroyAllWindows()