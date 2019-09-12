import numpy as np
import cv2 as cv

def click_event(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        img = param
        hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

        color = np.uint8([[img[y,x]]])
        hsv_color = cv.cvtColor(color, cv.COLOR_BGR2HSV)

        lower_range = np.asarray((hsv_color[0][0][0] - 10, 100, 100))
        upper_range = np.asarray((hsv_color[0][0][0] + 10, 255, 255))
        mask = cv.inRange(hsv, lower_range, upper_range)

        bit = cv.bitwise_and(img,img,mask=mask)
        cv.imshow('erhm', bit)


## Insert desired picture here
img = cv.imread('lighter.jpg')
cv.namedWindow('img')

## When user left clicks on the image, a new one will be displayed 
## that focuses on areas of the picture where the same color appears.
cv.setMouseCallback('img', click_event, img)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

while(1):
    cv.imshow('img', img)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()