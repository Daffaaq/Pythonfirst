import cv2
cam = cv2.VideoCapture(0)
while True:
    retV, frame = cam.read()
    cv2.imshow('Webcamku', frame)
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break
cam.release()
cv2.destryAllWindows