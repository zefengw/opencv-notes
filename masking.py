import cv2 as cv
import numpy as np

img = cv.imread("images/IMG_20210331_233608.jpg")
resize = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow("Resized", resize)
#Masking allows images to focus on certain parts of an image using bitwise operators

blank = np.zeros(resize.shape[:2], dtype="uint8")

#mask can be any circle
mask = cv.circle(blank, (resize.shape[1]//2 + 60, resize.shape[0]//2 - 75), 100, 255, -1)
cv.imshow("Mask", mask)

#shows image only in mask
masked = cv.bitwise_and(resize, resize, mask=mask)
cv.imshow("Masked Image", masked)




cv.waitKey(0)