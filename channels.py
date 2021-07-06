import cv2 as cv
import numpy as np

img = cv.imread("images/IMG_20210331_233608.jpg")
blank = np.zeros(img.shape[:2], dtype="uint8")
b,g,r = cv.split(img)
#Visible light has all colors of spectrum, which is why
#b,g, and r images look very similar
#Lighter images mean more of that color
blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])
cv.imshow("Blue", blue)
cv.imshow("Green", green)
cv.imshow("Red", red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

#Merged all colors
merged = cv.merge([b,g,r])
cv.imshow("Merged", merged)

cv.waitKey(0)