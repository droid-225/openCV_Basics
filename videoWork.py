import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0) # cap: capture, here 0 is for the primary webcam
#fourcc = cv2.VideoWriter_fourcc(*'XVID') # codex (encoding technique)
#out = cv2.VideoWriter("output.avi",fourcc,20.0,(640,480)) # (file name, codex, fps, window size)

while True:
    ret , frame = cap.read()
    flip = cv2.flip(frame,1)
    #img_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # convert footage to grayscale
    #out.write(frame)

    cv2.imshow("webcam",flip)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break;

#out.release()
cv2.destroyAllWindows()

# Playing video
#cap = cv2.VideoCapture('output.avi')

#while True:

    #ret , frame = cap.read()

    #time.sleep(1/20) # since video is 20 fps, it needs to be played back at a slower speed
    # sleep can be used to change speed of the video
    #cv2.imshow("webcam",frame)

    #if cv2.waitKey(1) & 0xFF == ord('x'):
        #break

#cv2.destroyAllWindows()