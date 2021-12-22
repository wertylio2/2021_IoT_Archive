import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('Camera open failed')
    exit()


face_cascade= cv2.CascadeClassifier('./xml/face.xml')
eye_cascade= cv2.CascadeClassifier('./xml/eye.xml')


while True:

    ret, frame = cap.read()
    frame = cv2.resize(frame, (640,360))
    if not ret:
        break
    faces = face_cascade.detectMultiScale(frame,1.3,5)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w, y+h),(255,0,0),2)

    cv2.imshow('frame',frame)

    if cv2.waitKey(10) == 27:
        break
cap.release()
cv2.destroyAllWindows()
