import cv2
import numpy as np
c=45
img=cv2.imread('image/download.jpeg',0)

height,width = img.shape
for i in range(height):
  for j in range(width):
    img[i,j] =np.clip(c*np.log(1+img[i,j]),0,255).astype('uint8')
cv2.imshow('log',img)
cv2.waitKey(0)
