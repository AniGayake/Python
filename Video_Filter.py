import cv2
import numpy as np


cap = cv2.VideoCapture(0)   # 0 for front webcam and 1 # for other
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('/home/rudra/codeChef/video.avi',fourcc,20.0,(640,480))
while True:
    ret ,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    out.write(frame)
    cv2.imshow('me',frame)
    cv2.imshow('grey',gray)

    if cv2.waitKey(1) & 0xFF ==  ord('q'):
        break


cap.release()
out.release()
cv2.waitKey(100)
cv2.destroyAllWindows()
