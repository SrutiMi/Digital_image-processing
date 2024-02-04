import cv2
import numpy as np

def log_transformation(image):
  c= 255/np.log(1+np.max(image))
  log_transformed = c*(np.log(image+1))

  # to avoid any ambiguity due to log(0) we have to add the following threshold
  # log_transformed[log_transformed > 255] = 255
  # log_transformed[log_transformed < 0] = 0
  return log_transformed.astype('uint8')

def image_subtraction(original_image,enhanced_image):
  subtracted_image = (np.abs(enhanced_image - original_image)).astype('uint8')
  return subtracted_image

def display_image(image,title):
  cv2.imshow(title,image)
  
original_image= cv2.imread('image/download.jpeg',cv2.IMREAD_GRAYSCALE)
enhanced_image=log_transformation(original_image)
display_image(enhanced_image,'Enhanced_image')

subtracted_image = image_subtraction(original_image,enhanced_image)
display_image(subtracted_image,'Subtracted_image')

cv2.waitKey(0)
cv2.destroyAllWindows()
