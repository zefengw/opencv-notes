#Contours are the boundaries of OBJECTS
import cv2 as cv
import numpy as np
img = cv.imread("images/IMG_20210331_233608.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray", gray)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
# cv.imshow("Blur", blur)

#edges
canny = cv.Canny(blur, 125, 175)
# cv.imshow("Canny", canny)

#threshold binarizes images
#take in gray image, intensity of pixel is below 125 set to black, and above 125 is white(255)
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow("Thresh", thresh)
#contours
#contours: list of all contours found in image, hierarchies: find the hierarchical contours
#RETR_TREE: hiearchical contours, RETR_EXTERNAL: external contours, RETR_LIST: all contours
#CHAIN_APPROX_NONE: all contours, CHAIN_APPROX_SIMPLE: output contours of endpoints
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f"{len(contours)} contours found")

blank = np.zeros(img.shape, dtype="uint8")
#something to draw on, contours list, contour index(-1 is all), color, thickness
cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow("Contours", blank)

cv.waitKey(0)
