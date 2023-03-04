import cv2
import numpy as np

img = cv2.imread("img/cliffs.jpg")

# Changing Brightness
#matrix = np.ones(img.shape, dtype = "uint8") * 50
# (img shape, data type) here uint8 means unsigned int 8 bit, * 50 makes it so all pixel intensities in the image are atleast 50

#img_bright = cv2.add(img,matrix)
#img_dark = cv2.subtract(img,matrix)

#mutli_img = np.hstack((img_bright,img,img_dark))

# Changing Contrast
# Constrast is the difference in intensity values of the pixels of an image
matrix1 = np.ones(img.shape) * .8 # Lower the number, lesser the contrast
matrix2 = np.ones(img.shape) * 1.2 # Higher the number, greater the contrast
# multiplying the image shapes gives them floating point values

img_lowCont = np.uint8(cv2.multiply(np.float64(img),matrix1))
#img_highCont = np.uint8(cv2.multiply(np.float64(img),matrix2))
# since image contains floating point values, the original image values have to be converted to 64 bit floats to multiply
# then the product is converted back into an uint8
# weird colors in high contrast image is due to the pixel values exceeding 255 and starting count from 0 again
img_highCont = np.uint8(np.clip(cv2.multiply(np.float64(img),matrix2),0,255))
# .clip function adds min and max values to the products, here it stops the values from exceeding 255

mutli_img = np.hstack((img_lowCont,img,img_highCont))
cv2.imshow("window",mutli_img)
cv2.waitKey(0)