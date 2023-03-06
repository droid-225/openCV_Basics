import cv2
import numpy as np
import time
import os
import urllib

if not os.path.isdir('model'):
  os.mkdir("model")

protoFile = "pose_deploy_linevec_faster_4_stages.prototxt"
weightsFile = "model/pose_iter_160000.caffemodel"

if not os.path.isfile(protoFile):
  # Download the proto file
  urllib.request.urlretrieve('https://raw.githubusercontent.com/CMU-Perceptual-Computing-Lab/openpose/master/models/pose/mpi/pose_deploy_linevec_faster_4_stages.prototxt', protoFile)

if not os.path.isfile(weightsFile):
  # Download the model file
  urllib.request.urlretrieve('http://posefs1.perception.cs.cmu.edu/OpenPose/models/pose/mpi/pose_iter_160000.caffemodel', weightsFile)

nPoints = 15
POSE_PAIRS = [[0,1], [1,2], [2,3], [3,4], [1,5], [5,6], [6,7], [1,14], [14,8], [8,9], [9,10], [14,11], [11,12], [12,13] ]
# Each point denotes a linkage in the human anatomy, 0 is the head and so on

net = cv2.dnn.readNetFromCaffe(protoFile, weightsFile)

im = cv2.imread("images/new-york.jpg")
inWidth = im.shape[1]
inHeight = im.shape[0]

netInputSize = (368, 368)
inpBlob = cv2.dnn.blobFromImage(im, 1.0 / 255, netInputSize, (0, 0, 0), swapRB = True, crop = False)
net.setInput(inpBlob)

# Forward Pass
output = net.forward()

# X and Y scale
scaleX = inWidth / output.shape[3]
scaleY = inHeight / output.shape[2]

# Empty list to store the detected keypoints
points = []

# Threshold
threshold = 0.1

for i in range(nPoints):
  # Obtain probability map
  probMap = output[0, i, :, :]

  # Find global maxima of the probMap
  minVal, prob, minLoc, point = cv2.minMaxLoc(probMap)

  # Scale the point to fit on the original image
  x = scaleX * point[0]
  y = scaleY * point[1]

  if prob > threshold:
    # Add the point to the list if the probability is greater than the threshold
    points.append((int(x), int(y)))
  else:
    points.append(None)

imPoints = im.copy()
imSkeleton = im.copy()
# Draw points
for i, p in enumerate(points):
  cv2.circle(imPoints, p, 8, (255, 255, 0), thickness=-1, lineType=cv2.FILLED)
  cv2.putText(imPoints, "{}".format(i), p, cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, lineType=cv2.LINE_AA)

# Draw skeleton
for pair in POSE_PAIRS:
  partA = pair[0]
  partB = pair[1]

  if points[partA] and points[partB]:
    cv2.line(imSkeleton, points[partA], points[partB], (255, 255, 0), 2)
    cv2.circle(imSkeleton, points[partA], 0, (255, 0, 0), thickness=-1, lineType=cv2.FILLED)

#cv2.imshow("points", imPoints)
cv2.imshow("Skeleton", imSkeleton)
cv2.waitKey(0)

