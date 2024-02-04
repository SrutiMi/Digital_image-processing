''' Write a program to perform colour separation into R, G and B from a colour image. Then use 
these R, G and B to convert the original colour image to its equivalent greyscale image. Display 
output images.'''

import cv2 
import numpy_tutorial as np

# doing color separation
def color_separation(image):

  #Initializing empty matrices for R,G,B channels
  red_channel = np.zeros_like(image)#creates a numpy array with the same shape and data type as the image

  green_channel= np.zeros_like(image)
  blue_channel = np.zeros_like(image)

  red_channel[:,:,0] = image[:,:,0]
  green_channel[:,:,1] =image[:,:,1]
  blue_channel[:,:,2]=image[:,:,2]

  return red_channel,green_channel,blue_channel


# doing conversion to grayscale

def convert_greyscale(image):
  grayscale_image =np.zeros(image.shape[:2],dtype=np.uint8)
  for i in range(image.shape[2]):
    grayscale_image+=image[:,:,i]*(i+1)

   # Normalize the grayscale image to 0-255 range
    grayscale_image = (grayscale_image / image.shape[2]).astype(np.uint8)

    return grayscale_image



color_image= cv2.imread('image/download.jpeg')
#separate the color channels
red,green,blue = color_separation(color_image)

#display the separated color channels 
cv2.imshow('Red channel',red)
cv2.imshow('Green channel',green)
cv2.imshow('Blue channel',blue)

gray_image = convert_greyscale(color_image)

# Display the grayscale image
cv2.imshow('Grayscale Image', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
