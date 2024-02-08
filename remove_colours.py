''' Write a program to (i) remove red colour (R) from a colour image (RGB image). 
Display the output images. 
(ii) remove blue colour (B) from a colour image. 
(iii) remove green colour (G) from a colour image. 
Display the output images'''

import cv2

def remove_red(image):
  img_without_red = image.copy()
  img_without_red[:,:,2]=0 # Setting the red channel to zero this way we are removing the red channel
  return img_without_red

def remove_green(image):
  img_without_green = image.copy()
  img_without_green[:,:,1]=0 # Setting the green channel to zero this way we are removing the green channel
  return img_without_green

def remove_blue(image):
  img_without_blue=image.copy()
  img_without_blue[:,:,0]=0 # Setting the blue channel to zero this way we are removing the blue channel
  return img_without_blue

img=cv2.imread('image/gfg.png')

# Removing the red channel
img_without_red =remove_red(img)
cv2.imshow('Image without red',img_without_red)

# Remove Blue Color
img_without_blue = remove_blue(img)
cv2.imshow('Image without blue',img_without_blue)

# Remove Green Color
img_without_green = remove_green(img)
cv2.imshow('Image without green',img_without_green)

cv2.waitKey(0)
cv2.destroyAllWindows()
