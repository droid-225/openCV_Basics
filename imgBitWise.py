import cv2
import numpy as np

# Bitwise operators can be used to combine two images
# Bitwise operators operate the same way as regular logic operators
# white can be taken as 255 and black as 0

#rect = cv2.imread("img/rectangle.jpg", cv2.IMREAD_GRAYSCALE)
#circ = cv2.imread("img/circle.jpg", cv2.IMREAD_GRAYSCALE)

# result = cv2.bitwise_and(rect,circ,mask=None) # bitwise and
# result = cv2.bitwise_or(rect,circ,mask=None) # bitwise or
#result = cv2.bitwise_xor(rect,circ,mask=None) # bitwise xor (exclusive or)

#cv2.imshow("result",result)
#cv2.imshow("rectangle",rect)
#cv2.imshow("circle",circ)
#cv2.waitKey(0)

# Logo Manipulation
coke = cv2.imread("img/coke.png",)
#coke = cv2.cvtColor(cokebgr,cv2.COLOR_BGR2RGB)
colors = cv2.imread("img/colors.png")
#colors = cv2.cvtColor(colorsbgr,cv2.COLOR_BGR2RGB) # might not need these two commented out codes, all they do is help make a better gray img

coke_gray = cv2.cvtColor(coke,cv2.COLOR_RGB2GRAY)
retval, coke_mask = cv2.threshold(coke_gray,127,255,cv2.THRESH_BINARY)

coke_mask_inv = cv2.bitwise_not(coke_mask) # bitwise not (all whites become black and wise versa)

colors_bg = cv2.bitwise_and(colors,colors,mask=coke_mask) # making colors the background

coke_fg = cv2.bitwise_and(coke,coke,mask=coke_mask_inv) # makes a foreground mask of the coke

result = cv2.add(colors_bg,coke_fg)

cv2.imshow("window",result)
cv2.waitKey(0)

