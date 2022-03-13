
import cv2 as cv
import numpy as np

img = cv.imread('in.jpg',0)
equ = cv.equalizeHist(img)
res = np.hstack((img, equ))
cv.imwrite('out.jpg',res)

