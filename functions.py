import cv2 as cv
img = cv.imread("images/IMG_20210331_233608.jpg")
# cv.imshow("Zefeng", img)

#Resize
#Interpolation: shrinking(cv.INTER_AREA) or enlarge(cv.INTER_LINEAR or cv.INTER_CUBIC)
resize = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow("Resized", resize)

#Grayscale image: Blue-green-red to gray
gray = cv.cvtColor(resize, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray", gray)

#Blur: image, blur dimensions, border
blur = cv.GaussianBlur(resize, (7,7), cv.BORDER_DEFAULT)
# cv.imshow("Blur", blur)

#Edge Cascade: input blur image to recognize less edges
canny = cv.Canny(resize, 125, 175)
# cv.imshow("Edges", canny)

#Dilating the image
dilated = cv.dilate(canny, (7,7), iterations=1)

#Eroding: undo dilation
eroded = cv.erode(dilated, (7,7), iterations=2)

#Cropping
cropped = img[50:200, 200:400]
cv.imshow("Cropped", cropped)

cv.waitKey(0)