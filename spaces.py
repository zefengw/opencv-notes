import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("images/IMG_20210331_233608.jpg")

#Matplotlib displays images as RGB, an inversion of colors
# plt.imshow(img)
# plt.show()

#Can convert images back to BGR
#BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray", gray)

# #BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow("HSV", hsv)

# #BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
# cv.imshow("Lab", lab)

#BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("RGB", rgb)

cv.waitKey(0)