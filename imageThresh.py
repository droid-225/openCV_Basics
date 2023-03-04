import cv2
import numpy as np

#img = cv2.imread("img/windows.jpg", cv2.IMREAD_GRAYSCALE)
#retval, img_thresh = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY) # makes binary map from image

#multi_img = np.hstack((img,img_thresh))
#cv2.imshow("window", multi_img)
#cv2.waitKey(0)

# Sheet Music Reader
img = cv2.imread("img/music.png", cv2.IMREAD_GRAYSCALE)

# These two use global thresholds
retval, img_thresh1 = cv2.threshold(img,50,255,cv2.THRESH_BINARY) # Threshold is too low to get notes in top
retval, img_thresh2 = cv2.threshold(img,130,255,cv2.THRESH_BINARY) # Threshold is too high and causes bottom left to be black

# This uses an adaptive threshold
img_thresh3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,7) # Find mean value of threshold required to better isolate all the notes

multi_img = np.hstack((img,img_thresh1))
multi_img2 = np.hstack((img_thresh2,img_thresh3))
cv2.imshow("window",multi_img)
cv2.imshow("window2",multi_img2)
cv2.waitKey(0)

