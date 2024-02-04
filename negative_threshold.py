import cv2
import numpy as np

def image_negative(image):
  max_pixel_value =255
  negative_image = max_pixel_value - image
  return negative_image

def image_thresholding(image,threshold):
  # threshold_image =np.where(image>threshold,255,0) if the image's pixel values are >threshold then apply 255 otherwise 0

  # without using np.where()

  threshold_image =image.copy()#this ensures that we are not directly modifying the image
  # and we are creating a copy of the image

  threshold_image[image > threshold] =255
  threshold_image[image <= threshold] =0

  return threshold_image.astype('uint8')

def display_image(image,title):
  cv2.imshow(title,image)
  cv2.waitKey(0)
  cv2.destroyAllWindows()

original_image=cv2.imread('image/lowcontrast.jpeg',cv2.IMREAD_GRAYSCALE)

display_image(original_image,'original image')

negative_result = image_negative(original_image)
display_image(negative_result, 'Image Negative')

threshold_value =150
threshold_result = image_thresholding(original_image,threshold_value)
display_image(threshold_result, 'Image Thresholding')