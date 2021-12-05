import numpy as np
import cv2
import face_recognition
import time
import datetime
import RPi.GPIO as GPIO

cap = cv2.VideoCapture(1)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_fullbody.xml")
detection = True
detection_stopped_time = None
timer_started = False
RECORD_AFTER_DETECTION = 5


frame_size = (int(cap.get(3)), int(cap.get(4)))
fourcc = cv2.VideoWriter(*".mp4v")
out = cv2.VideoWriter("Video.mp4", fourcc, 20.0, frame_size)



while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    body = body_cascade.detectMultiScale(gray, 1.3, 5)

    if len(faces) + len(body) > 0:
        if detection:
            timer_started = False
        else:
            detection = True
    out.write(frame)
    
    for (x, y, width, height) in faces:
        cv2.rectangle(frame, (x,y), (x+width, y+height), (255,0,0), 3) # draw a rectangle on the image from the variable called frome, so the (x,y) statement points
                                                                       # where x represents the top right corner and y represents the bottom left corner. The next statement
                                                                       # (x+width, y+height) helps to form a rectangle. The next part of the code is for colour (format: Blue, Green, Red) and thickness.
        

    
    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) == ord('q'):
        break

out.release()
cap.release()
cv2.destroyAllWindows()