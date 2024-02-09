import cv2
import numpy as np
import matplotlib.pyplot as plt 
def contrast_stretching(image):
  bit_depth=image.dtype.itemsize*8
  min_pixel = np.min(image)
  max_pixel = np.max(image)
  Lmax=(2**bit_depth)-1
  Lmin=0
  # contrast_stretched = (image-min_pixel)/(max_pixel-min_pixel)*255
  contrast_stretched = (image-min_pixel)/(max_pixel-min_pixel)*(Lmax-Lmin)+Lmin
  return contrast_stretched.astype('uint8')
  # contrast_image=(((Lmax-Lmin)*(image-min_pixel))/(max_pixel-min_pixel)) +Lmin
  # return contrast_image.astype('uint8')

image = cv2.imread('image/lowcontrast.jpeg')
contrast_stretched = contrast_stretching(image)
cv2.imshow('Original',image)
cv2.imshow('Contrast Stretched',contrast_stretched)
cv2.waitKey(0)

# Display using matplotlib
fig, axes = plt.subplots(1, 2, figsize=(10, 5))
axes[0].imshow(image, cmap='gray')
axes[0].set_title("Original Image")

axes[1].imshow(contrast_stretched, cmap='gray')
axes[1].set_title("Stretched Image")

plt.show()

