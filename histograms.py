import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("images/IMG_20210331_233608.jpg")
resize = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)

#histogram: visual pixel intensity distributions
#gray histogram
gray = cv.cvtColor(resize, cv.COLOR_BGR2GRAY)

blank = np.zeros(resize.shape[:2], dtype="uint8")

mask = cv.circle(blank, (resize.shape[1]//2, resize.shape[0]//2), 100, 255, -1)

masked = cv.bitwise_and(gray, gray, mask=mask)
# cv.imshow("Mask", masked)
#gives histogram of the particular mask
gray_hist = cv.calcHist([gray], [0], mask, [256], [0,256])

plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

#colour histogram
plt.figure()
plt.title("Colour Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
colors = ("b", "g", "r")
for i,col in enumerate(colors):
    #histogram for bgr in mask
    hist = cv.calcHist([resize], [i], mask, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])
plt.show()

cv.waitKey(0)