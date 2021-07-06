import cv2 as cv

#haar cascades are more popular but are not the most advanced
img = cv.imread("images/Testing Photo ID.jpg")
img = cv.resize(img, (500,500),interpolation=cv.INTER_CUBIC)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#read all xml code
haar_cascade = cv.CascadeClassifier("haar_face.xml")

#haar_cascades are really sensitive to noise in image
#minNeighbors controls how sensitive the detection is to faces
# higher->less sensitive, lower->more sensitive
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

print(f"Number of faces found = {len(faces_rect)}")

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)
cv.imshow("Detected Face", img)


cv.waitKey(0)