import cv2 as cv
import numpy as np

#Shape of 500 by 500 and with 3 color channels(blue, green, red)
# and with a data type of uint8(image)
blank = np.zeros((500, 500, 3), dtype="uint8")
# cv.imshow("Blank", blank)

#Paint Image a certain colour
#Access all frames of blank
# blank[:] = 255, 0, 0
#200 to 400 pixels: up-to-down
#300 to 400 pixels: left to right
blank[200:400, 300:400] = 0, 0, 255
# cv.imshow("Red", blank)

#Draw Rectangle
#Imge, top-left corner, bottom-right corner, color, border thickness(e.g., thickness=2)
#cv.FILLED = -1 for thickness     divides shapes by 2 for x and y
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0, 0, 255), thickness=cv.FILLED)
# cv.imshow("Rectangle", blank)

#Draw Circle
#Image, midpoint, radius, color, thickness(same as rectangle)
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (255, 0,0), thickness=2)
# cv.imshow("Circle", blank)
#Draw Line
#image, start point, end point, color,
cv.line(blank, (0,0), (400, 500), (255, 255, 255), thickness=3)
# cv.imshow("Line", blank)

#Write Text
#image, text, coordinate, font, font scale, color, thickness
cv.putText(blank, "Hello, I'm a crackhead", (0, 255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255,0), 2)
cv.imshow("Text", blank)
cv.waitKey(0)