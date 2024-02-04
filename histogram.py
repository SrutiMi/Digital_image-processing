import cv2
import numpy as np
import matplotlib.pyplot as plt

def compute_display_histogram(image_path):
  img =cv2.imread(image_path,cv2.IMREAD_GRAYSCALE)
  

  # initializing an array to store the histogram

  histogram = np.zeros(256,dtype=int)# here we are initializing an array of 256 elements with 0 as we know in a grayscale image the intensities are from 0 to 255

  # calculating the histogram
  for row in img:
    for pixel_value in row:
      histogram[pixel_value] += 1

  # plotting the histogram
  plt.plot(histogram,color = 'black',)
  plt.xlabel('Pixel value')
  plt.ylabel('Frequency')
  plt.title('Histogram')
  plt.show()


image_path = 'image/lowcontrast.jpeg'
compute_display_histogram(image_path)

