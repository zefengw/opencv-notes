import cv2 as cv
import numpy as np
img = cv.imread("images/IMG_20210331_233608.jpg")

#Translation
def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x -> left
# -y -> up
# x -> right
# y -> down

translated = translate(img, 100, 100)
# cv.imshow("Translated", translated)

#Rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2, height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)

#Can constantly rotate the same image
#but it will cut the image as you rotate it
rotated = rotate(img, 45)
# cv.imshow("Rotated", rotated)

# Resizing
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
# cv.imshow("Resized", resized)

#Flip
#image, (0: flip image over x-axis, 1: flip image over y-axis, -1: flip image over both x and y axis)
flip = cv.flip(resized, 0)
# cv.imshow("Flipped", flip)

#Cropping
cropped = resized[200:400, 300:400]
cv.imshow("Cropped", cropped)

cv.waitKey(0)