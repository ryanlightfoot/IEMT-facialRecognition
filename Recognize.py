import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') #Face data
cap = cv2.VideoCapture(0) #Get capture decive
while True:
    ret, img = cap.read(1) #Read capture device
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Convert image to greyscale
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) #Detect faces from greyscale
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255,165,0), 2) #Draw rectangle of the face
    cv2.imshow('image window', img) #Show image
    k = cv2.waitKey(30) & 0xff #Frame
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()