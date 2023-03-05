import cv2
import numpy as np
import glob
import math

# Read images
boats = glob.glob("img/boat/*")
boats.sort()

imgs = []
for filename in boats:
    img = cv2.imread(filename)
    imgs.append(img)

num_imgs = len(imgs)

num_cols = 3
num_rows = math.ceil(num_imgs / num_cols)

# Stitch images
stitcher = cv2.Stitcher_create()
status, result = stitcher.stitch(imgs)
if status == 0:
    cv2.imshow("Pano", result)

cv2.waitKey(0)


