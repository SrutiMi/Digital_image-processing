import cv2
import numpy as np

def enhance_brightness(image,alpha):
  img=image.copy()
  enhanced_img =np.clip(img*alpha,0,255).astype(np.uint8)
  return enhanced_img

def supress_brightness(image,beta):
  img=image.copy()
  enhanced_img=np.clip(img+beta,0,255).astype(np.uint8)
  return enhanced_img

def manipulate_contrast(image,alpha,beta):
  img=image.copy()
  contrast = np.clip(img*alpha+beta,0,255).astype('uint8')
  return contrast

img=cv2.imread('image/download.jpeg')
alpha =1.5
beta =-55

enhanced_img=enhance_brightness(img,alpha)
supressed=supress_brightness(img,beta)
contrast_img=manipulate_contrast(img,alpha,beta)

cv2.imshow("brightness",enhanced_img)
cv2.imshow("contrast",contrast_img)
cv2.imshow("supressed",supressed)
cv2.waitKey(0)