import cv2 as cv
img = cv.imread("images/IMG_20210331_233608.jpg")
resize = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)

#Simple thresholding: manually setting a threshold value
gray = cv.cvtColor(resize, cv.COLOR_BGR2GRAY)

#threshold: the same threshold value: 150
#thresh: binarized image
#pixel intensity between 150 and 255 turns to 1(white)
#and anything not in between is set to 0(black)
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
# cv.imshow("Threshhold", thresh)

# pixel intensity between 150 and 255 turns to 0(black) and vice versa
threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
# cv.imshow("Threshhold Inverse", thresh_inv)

#Adaptive Thresholding: letting computer finding the right threshold value
#cv.ADAPTIVE_THRESH_GAUSSIAN_C: puts weight on every pixel
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow("Adaptive", adaptive_thresh)

cv.waitKey(0)