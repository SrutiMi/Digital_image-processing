import cv2
import numpy as np

def add_salt_and_pepper(img,salt,pepper):
  noisy=img.copy()
  row,col= noisy.shape
  salt_pixel= np.random.rand(row,col)<salt
  noisy[salt_pixel]=255

  pepper_pixel=np.random.rand(row,col)<pepper
  noisy[pepper_pixel]=0

  return noisy

org_img=cv2.imread('image/3.jpg',0)
salt=0.02
paper=0.02
noisy_img=add_salt_and_pepper(org_img,salt,paper)
cv2.imshow("Noisy Image",noisy_img)
cv2.waitKey(0)