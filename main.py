import cv2
import numpy as np

# Simplest image is black and white (2 channel: pixel could have a value of 0 or 1)
# Grayscale image: pixel can have value from 0 to 255 to make the image look black white and grey (gradient between black and white)
# Colored Image: 3 channels: RGB, three channels (layers) in which pixel can have value between 0 and 255
# uncomment img on line 10 for the codes to work

# Read an image
#img = cv2.imread("img/mush.png")
# print(img) # prints numpy matrix values of img
# print(img.shape) # prints resolution of image and number of channels
#cv2.imshow("window", img) # displays image
#cv2.waitKey(0) # adds infinite delay to image to keep it open until user closes the window

# Converting to grayscale
#img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # converts RGB(BGR in openCV) to grayscale
#print(img_gray.shape)
#cv2.imshow("window", img_gray) # displays image
#cv2.waitKey(0) # adds infinite delay to image to keep it open until user closes the window

# Playing with RGB color channels
#img[:,:,0] = 0 # Removes all blue from the image (blue channel is 0)
#img[:,:,1] = 0 # Removes all green from the image (green channel is 0)
#img[:,:,2] = 0 # Removes all red from the image (red channel is 0)
#imgBlue = img[:,:,0] # blue channel
#imgGreen = img[:,:,1] # green channel
#imgRed = img[:,:,2] # red channel
#new_img = np.hstack((imgBlue,imgGreen,imgRed)) # puts three images side by side (can be more or less than three)
#cv2.imshow("window", new_img) # displays image
#cv2.waitKey(0) # adds infinite delay to image to keep it open until user closes the window

# Resizing image
#img_resize = cv2.resize(img, (500,500)) # (image, new size) new size can be bigger and smaller than the given image
#img_resize = cv2.resize(img, (img.shape[1]//2, img.shape[0]//2)) # halfs size of img
#cv2.imshow("window", img_resize)
#cv2.waitKey(0)

# Flip image
#img_flip = cv2.flip(img,-1)
# flip function has three codes:
# 0 flips img upside down (about horizontal axis)
# 1 flips img about vertical axis
# -1 does both
#cv2.imshow("window", img_flip)
#cv2.waitKey(0)

# Cropping
#img_crop = img[50:300,250:500] # [y start: y end, x start: x end] with origin at top left corner of image
# going across the image left to right is called its width
# going up and down the image vertically is called its height
# Saving img
#cv2.imwrite('fruits_small.png', img_crop)
#cv2.imshow("window", img_crop)
#cv2.waitKey(0)

# Drawing shapes and texts
#img = np.zeros((512,512,3)) # Creates black image with given size and channels
# Rectangle
#cv2.rectangle(img,pt1=(100,100),pt2=(300,300),color=(255,0,0),thickness=3)
# rectangle(image,(top left point),(bottom right point),color,thickness)
# to fill the rectangle, thickness = -1

# Circle
#cv2.circle(img,center=(100,400),radius=50,color=(0,0,255),thickness=3)
# rectangle(image,(center point),radius,color,thickness)
# to fill circle, thickness = -1

# Line
#cv2.line(img,pt1=(0,0),pt2=(512,512),thickness=2,color=(0,255,0))
# rectangle(image,(start point),(end point),thickness,color)

# Text
#cv2.putText(img,org=(100,100),fontScale=3,color=(0,255,255),thickness=2,lineType=cv2.LINE_AA,text="Hello",fontFace=cv2.FONT_ITALIC)
# org is the top left point of text box
# fontScale controls the size of the text

#cv2.imshow('window',img)
#cv2.waitKey(0)

# Events
#flag = False
#ix = -1 # current location of x
#iy = -1 # current location of y

#def draw(event,x,y,flags,params): # x and y are the coordinates of the mouse
    #global flag,ix,iy

    # draw circles on click
    #if event == 1:
        #cv2.circle(img,center=(x,y),radius=50,color=(0,0,255),thickness=-1)
    # draw rectangle
    #if event == 1: # on click
        #flag = True
        #ix = x
        #iy = y
    #elif event == 0: # on movement
        #if flag == True:
            #cv2.rectangle(img,pt1=(ix,iy),pt2=(x,y),color=(0,255,255),thickness=-1)

    #elif event == 4: # on release
        #flag = False
        #cv2.rectangle(img,pt1=(ix,iy),pt2=(x,y),color=(0,255,255),thickness=-1)

#cv2.namedWindow(winname = "window") # winname = window name
#cv2.setMouseCallback("window",draw) # mouse listener

#img = np.zeros((512,512,3))

#while True:
    #cv2.imshow("window",img)

    #if cv2.waitKey(1) & 0xFF == ord('x'): # 0xFF is keyboard input, ord(key), here the window only closes if x is pressed on the keyboard
        #break

#cv2.destroyAllWindows()

# Cropping Tool
img = cv2.imread("img/mush.png")

flag = False
ix = -1
iy = -1
def crop(event,x,y,flags,params):
    global flag,ix,iy

    if event == 1:
        flag = True
        ix = x
        iy = y

    elif event == 4:
        fx = x
        fy = y
        flag = False
        cv2.rectangle(img,pt1=(ix,iy),pt2=(x,y),thickness=1,color=(0,0,0))
        # Cropping
        cropped = img[iy:fy,ix:fx]
        cv2.imshow("new_window",cropped)
        cv2.waitKey(0)

cv2.namedWindow(winname="window")
cv2.setMouseCallback("window",crop)

while True:
    cv2.imshow("window",img)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cv2.destroyAllWindows()


