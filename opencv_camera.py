import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('Camera open failed')
    exit()


while True:

    ret, frame1 = cap.read()
    frame1 = cv2.resize(frame1, (320,240))
    if not ret:
        break
    frame2 = cv2.Canny(frame1,0,100)
    frame3 = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',frame1)
    cv2.imshow('edge',frame2)
    cv2.imshow('gray',frame3)

    if cv2.waitKey(10) == 27:
        break
cap.release()
cv2.destroyAllWindows()