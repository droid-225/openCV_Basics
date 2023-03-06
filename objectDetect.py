import os
import cv2
import numpy as np
import urllib
import tarfile

# Architecture: Mobilenet based Single Shot Multi-Box (SSD)
# Framework: Tensorflow

modelFile = "models/ssd_mobilenet_v2_coco_2018_03_29/frozen_inference_graph.pb"
configFile = "models/ssd_mobilenet_v2_coco_2018_03_29.pbtxt"
classFile = "coco_class_labels.txt"

if not os.path.isdir('models'):
    os.mkdir("models")

if not os.path.isfile(modelFile):
    os.chdir("models")

    # Download the tensorflow model
    urllib.request.urlretrieve(
        'http://download.tensorflow.org/models/object_detection/ssd_mobilenet_v2_coco_2018_03_29.tar.gz',
        'ssd_mobilenet_v2_coco_2018_03_29.tar.gz')

    # Uncompress the file
    file = tarfile.open('ssd_mobilenet_v2_coco_2018_03_29.tar.gz')
    #!tar - xvf ssd_mobilenet_v2_coco_2018_03_29.tar.gz
    file.extractall('./openCV_Basics')
    file.close()

    # Delete the tar.gz file
    os.remove('ssd_mobilenet_v2_coco_2018_03_29.tar.gz')

    # Come back to the previous directory
    os.chdir("..")

# Check Class Labels
with open(classFile) as fp:
    labels = fp.read().split("\n")

# Steps for performing inference using a DNN model:
# 1. Load the model and input image into memory
# 2. Detect objects using a forward pass through the network
# 3. Display the detected objects with bounding boxes and class labels

# Read the Tensorflow network
net = cv2.dnn.readNetFromTensorflow(modelFile, configFile)

# For ach file in the directory
def detect_objects(net, img):
    dimg = 300

    # Create a blob from the image
    blob = cv2.dnn.blobFromImage(img, 1.0, size=(dimg, dimg), mean=(0,0,0), swapRB = False, crop = False)

    # Pass blob to the network
    net.setInput(blob)

    # Perform prediction
    objects = net.forward()
    return objects

def display_text(im, text, x, y):

    # Get text size
    textSize = cv2.getTextSize(text, FONTFACE, FONT_SCALE, THICKNESS)
    dim = textSize[0]
    baseline = textSize[1]

    # Use text size to create a black rectangle
    cv2.rectangle(im, (x,y-dim[1] - baseline), (x + dim[0], y + baseline), (0,0,0), cv2.FILLED);
    # Display text inside the rectangle
    cv2.putText(im, text, (x, y-5 ), FONTFACE, FONT_SCALE, (0, 255, 255), THICKNESS, cv2.LINE_AA)


FONTFACE = cv2.FONT_HERSHEY_SIMPLEX
FONT_SCALE = 0.7
THICKNESS = 1


def display_objects(im, objects, threshold=0.25):
    rows = im.shape[0];
    cols = im.shape[1]

    # For every Detected Object
    for i in range(objects.shape[2]):
        # Find the class and confidence
        classId = int(objects[0, 0, i, 1])
        score = float(objects[0, 0, i, 2])

        # Recover original cordinates from normalized coordinates
        x = int(objects[0, 0, i, 3] * cols)
        y = int(objects[0, 0, i, 4] * rows)
        w = int(objects[0, 0, i, 5] * cols - x)
        h = int(objects[0, 0, i, 6] * rows - y)

        # Check if the detection is of good quality
        if score > threshold:
            display_text(im, "{}".format(labels[classId]), x, y)
            cv2.rectangle(im, (x, y), (x + w, y + h), (255, 255, 255), 2)

    cv2.imshow("image", im)
    cv2.waitKey(0)

im = cv2.imread('images/soccer.jpg')
objects = detect_objects(net, im)
display_objects(im, objects)
