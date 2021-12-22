import cv2

model = './dnn/res10_300x300_ssd_iter_140000_fp16.caffemodel'
config = './dnn/face_deploy.prototxt'

cap = cv2.VideoCapture(0)
net = cv2.dnn.readNet(model, config)

while True:
    _, frame = cap.read()
    frame = cv2.resize(frame, (640,360))
    if frame is None:
        break

    blob = cv2.dnn.blobFromImage(frame, 1, (300,300),(104,117,123))
    net.setInput(blob)

    detect = net.forward()
    detect = detect[0,0,:,:]

    (h,w) = frame.shape[:2]

    for i in range(0,detect.shape[0]):
        confidence = detect[i,2]
        if confidence < 0.5:
            break

        x1 = int(detect[i,3] * w)
        y1 = int(detect[i,4] * h)
        x2 = int(detect[i,5] * w)
        y2 = int(detect[i,6] * h)

        cv2.rectangle(frame, (x1,y2),(x2,y2),(0,255,0))
        label = 'Face : %4.3f'%confidence
        cv2.putText(frame, label, (x1,y1-1),cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0),2)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()