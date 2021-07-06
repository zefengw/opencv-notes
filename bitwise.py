import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype="uint8")
rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)

cv.imshow("Rectangle", rectangle)
cv.imshow("Circle", circle)

#bitwise AND: returned intersecting regions of the two images
bitwise_and = cv.bitwise_and(rectangle, circle)
# cv.imshow("AND", bitwise_and)

#bitwise OR: returned non-intersecting and intersecting regions
bitwise_or = cv.bitwise_or(rectangle, circle)
# cv.imshow("OR", bitwise_or)

#bitwise XOR: returned non-intersecting regions(opposite of AND)
bitwise_xor = cv.bitwise_xor(rectangle, circle)
# cv.imshow("XOR", bitwise_xor)

#bitwise NOT: returned the inverted regions of the image: black --> white and vice versa
bitwise_not = cv.bitwise_not(rectangle)
# cv.imshow("NOT", bitwise_not)


cv.waitKey(0)