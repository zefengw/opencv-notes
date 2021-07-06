import cv2 as cv
img = cv.imread("images/IMG_20210331_233608.jpg")

#Averaging
#(3,3) is the kernal size, kind of like a grid where
#the surrounding square intensity of the kernal is
# summed up and averaged to create the blur for the middle
# the kernal travels around the image
# the larger the dimensions the more blurry
average = cv.blur(img, (7,7))
# cv.imshow("Average Blur", average)

# Gaussian Blur
# Same thing as averaging except it computes average of all
# surrounding pixel intensity
# tend to get less blurring but is more natural
# (7,7)
gauss = cv.GaussianBlur(img, (7,7),0)
# cv.imshow("Gaussian Blur",gauss)

#Median Blur
#Same thing as Averaging except it finds median of surrounding pixels
#Integer because it assumes it will be a 3 by 3

median = cv.medianBlur(img, 3)

#Bilateral
#The most effective blurring because it retains the edges
bilateral = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow("Bilateral", bilateral)



cv.waitKey(0)
