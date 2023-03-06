import cv2
import numpy as np
import matplotlib.pyplot as plt

def readImagesAndTimes():
    # List of file names
    filenames = ["img/dark.jpg","img/lessDark.jpg","img/mid.jpg","img/bright.jpg"]

    # List of exposure times
    times = np.array([1/30.0, 0.25, 2.5, 15.0], dtype=np.float32)

    # Read images
    images = []
    for filename in filenames:
        img = cv2.imread(filename)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        images.append(img)

    return images, times

# Read images and exposure times
images, times = readImagesAndTimes()

# Align Images
alignMTB = cv2.createAlignMTB() # MTB: medium threshold bitmap
alignMTB.process(images, images)

# Find Camera Response Function (CRF)
calibrateDebevec = cv2.createCalibrateDebevec()
responseDebevec = calibrateDebevec.process(images, times)

# Merge images into an HDR linear image
mergeDebevec = cv2.createMergeDebevec()
hdrDebevec = mergeDebevec.process(images, times, responseDebevec)

# Tonemap using Drago's method to obtain 24-bit color image
tonemapDrago = cv2.createTonemapDrago(1.0,0.7)
ldrDrago = tonemapDrago.process(hdrDebevec)
ldrDrago = 3 * ldrDrago
#cv2.imwrite("ldr-Drago.jpg", ldrDrago * 255)
#print("saved")

# Tonemap using Reinhard's method to obtain 24-bit color image
toneMapReinhard = cv2.createTonemapReinhard(1.5,0,0,0)
ldrReinhard = toneMapReinhard.process(hdrDebevec)
#cv2.imwrite("img/ldrReinhard.jpg", ldrReinhard * 255)
#print("saved")

# Tonemap using Mantiuk's method to obtain 24-bit color image
toneMapMantiuk = cv2.createTonemapMantiuk(2.2,0.85,1.2)
ldrMantuik = toneMapMantiuk.process(hdrDebevec)
ldrMantuik = 3 * ldrMantuik
cv2.imwrite("img/ldrMantuik.jpg", ldrMantuik * 255)
print("saved")