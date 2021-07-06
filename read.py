import cv2 as cv
#Size of Images
#Reading Images:
#Reads image frames
img = cv.imread('images/IMG_20210331_233608.jpg')
#Displays Image
cv.imshow("Zefeng", img)

#Default scaling of 75%
def rescaleFrame(frame, scale=0.75):
    #Images, Videos, and Live Video
    #frame.shape[1] is the width of the image
    width = int(frame.shape[1] * scale)
    #frame.shape[0] is the height of the image
    height = int(frame.shape[0] * scale)
    #Tuple containing of width and height
    dimensions = (width, height)
    #Resizes frame
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


#Waits for a delay for a key to be pressed.
#Passing in 0 means it will wait an infinite amount of time
cv.waitKey(0)

#Create a resized image to fit more onto your window screen
resized_image = rescaleFrame(img)
cv.imshow("Haha", resized_image)

def changeRes(width, height):
    #Live Videos
    #3 references width
    capture.set(3, width)
    #4 references height
    capture.set(4, height)

#Reading Videos:
#Webcam: pass in 0, First Camera: 1, Second Camera: 2 etc
capture = cv.VideoCapture("videos/Charify Demo.mp4")
while True:
    #Reads video frame-by-frame
    isTrue, frame = capture.read()
    frame_resize = rescaleFrame(frame)
    #display each individual frame
    cv.imshow("Video", frame)
    cv.imshow("Video Resize", frame_resize)
    #Breaks if letter d is pressed and waits 20 seconds for you to press a key
    if cv.waitKey(20) & 0xFF==ord("d"):
        break
#Video will throw Assertion error if video timer ends and
#can't find any more frames, stating that it can't find media
#at a specific location. The same is for images that can't be read
capture.release()
cv.destroyAllWindows()


