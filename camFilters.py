import cv2
import numpy

PREVIEW = 0
BLUR = 1
FEATURES = 2
CANNY = 3

feature_params = dict(maxCorners = 500,
                       qualityLevel = 0.2,
                       minDistance = 15,
                       blockSize = 9)
# maxCorners = maximum amount of corners the output can show
# qualityLevel = minimum quality level of corners
# minDistance = minimum distance between feature corners (euclidian distance in pixel space)
# blockSize = size of the pixel neighborhood

cap = cv2.VideoCapture(0) # cap: capture, here 0 is for the primary webcam
image_filter = CANNY

while True:
    ret , frame = cap.read()
    frame = cv2.flip(frame,1)

    if image_filter == PREVIEW:
        result = frame
    elif image_filter == CANNY:
        result = cv2.Canny(frame,80,150)
    elif image_filter == BLUR:
        result = cv2.blur(frame,(13,13)) # (13,13) is the dimensions of box kernal, bigger box more blur, smaller box less blur
    elif image_filter == FEATURES:
        result = frame
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        corners = cv2.goodFeaturesToTrack(frame_gray, **feature_params)
        if corners is not None:
            for x, y in numpy.float32(corners).reshape(-1, 2):
                cv2.circle(result, (int(x), int(y)), 10, (0, 255, 0), 1)

    cv2.imshow("webcam", result)

    key = cv2.waitKey(1)
    if key == ord('x') or key == 27:
        break;
    elif key == ord('c'):
        image_filter = CANNY
    elif key == ord('b'):
        image_filter = BLUR
    elif key == ord('f'):
        image_filter = FEATURES
    elif key == ord('p'):
        image_filter = PREVIEW

cv2.destroyAllWindows()