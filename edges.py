import cv2 as cv
import numpy as np
img = cv.imread("images/IMG_20210331_233608.jpg")
resize = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)

gray = cv.cvtColor(resize, cv.COLOR_BGR2GRAY)

#Loplacian: gradients of image
lap = cv.Laplacian(gray, cv.CV_64F)
#absolute value of image pixels, and then converted into an unsigned byte
lap = np.uint8(np.absolute(lap))
# cv.imshow("Laplacian", lap)

#Sobel: gradients across x and y axis
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, +0, 1)
combined_sobel = cv.bitwise_or(sobelx, sobely)
# cv.imshow("SobelX", sobelx)
# cv.imshow("SobelY", sobely)
# cv.imshow("Combined", combined_sobel)

#Canny: multi-stage process, cleaner
canny = cv.Canny(gray, 150, 175)
cv.imshow("Canny", canny)





cv.waitKey(0)