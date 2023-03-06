import cv2
import sys
import os
import numpy as np
from IPython.display import HTML
import urllib

# Needs to be fixed

# Tracking Algorithms in openCV:
# BOOSTING
# MIL
# KCF
# CRST
# TLD - Tends to recover from occulusions
# MEDIANFLOW - Good for predictable slow motion
# GOTURN - Deep learning based, most accurate
# MOSSE - Fastest

video_name = "vid/race_car.mp4"

def drawRectangle(frame, bbox): # bbox: bounding box
    p1 = (int(bbox[0]), int(bbox[1]))
    p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
    cv2.rectangle(frame, p1, p2, (255,0,0),2,1)

def displayRectangle(frame, bbox):
    frameCopy = frame.copy()
    drawRectangle(frameCopy, bbox)
    frameCopy = cv2.cvtColor(frameCopy, cv2.COLOR_RGB2BGR)
    cv2.imshow("car", frameCopy)

def drawText(frame, txt, location, color = (50,170,50)):
    cv2.putText(frame, txt, location, cv2.FONT_HERSHEY_SIMPLEX, 1, color, 3)

# Set up tracker
tracker_types = ['BOOSTING', 'MIL']

# Change the index to change the tracker type
tracker_type = tracker_types[0]

if tracker_type == 'BOOSTING':
    tracker = cv2.legacy_TrackerBoosting.create()
elif tracker_type == 'MIL':
    tracker = cv2.TrackerMIL_create()

# Read video
video = cv2.VideoCapture(video_name)
ok, frame = video.read()

# Exit if video is not opened
if not video.isOpened():
    print("Could not open video")
    sys.exit()
else:
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

video_out_name = 'race_car-' + tracker_type + '.mp4'
video_out = cv2.VideoWriter(video_out_name, cv2.VideoWriter_fourcc(*'avc1'), 10, (width, height))

# Define bounding box
bbox = (1300, 405, 160, 120)
displayRectangle(frame, bbox)

# Initialize tracker with first frame and bounding box
ok = tracker.init(frame, bbox)

while True:
    ok, frame = video.read()
    if not ok:
        break

    # Start timer
    timer = cv2.getTickCount()

    # Update tracker
    ok, bbox = tracker.update(frame)

    # Calculate FPS
    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)

    # Draw bounding box
    if ok:
        drawRectangle(frame, bbox)
    else:
        drawText(frame, "Tracking failure detected", (80,140), (0,0,255))

    # Display info
    drawText(frame, tracker_type + " Tracker", (80,160))
    drawText(frame, "FPS: " + str(int(fps)), (80,100))

    # Write frame to video
    video_out.write(frame)

video.release()
video_out.release()

# Tracker: KCF
HTML("""
<video width=1024 controls>
  <source src="race_car-KCF.mp4" type="video/mp4">
</video>
""")

