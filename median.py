# Median Spatial Domain Filtering 


import cv2 
import numpy as np 


# Read the image 
img_noisy1 = cv2.imread('image/filter.png', 0) 

# Obtain the number of rows and columns 
# of the image 
m, n = img_noisy1.shape 

# Traverse the image. For every 3X3 area, 
# find the median of the pixels and 
# replace the center pixel by the median 
img_new1 = np.zeros([m, n]) 

for i in range(1, m-1): 
	for j in range(1, n-1): 
		temp = [img_noisy1[i-1, j-1], 
			img_noisy1[i-1, j], 
			img_noisy1[i-1, j + 1], 
			img_noisy1[i, j-1], 
			img_noisy1[i, j], 
			img_noisy1[i, j + 1], 
			img_noisy1[i + 1, j-1], 
			img_noisy1[i + 1, j], 
			img_noisy1[i + 1, j + 1]] 
		
		temp = sorted(temp) 
		img_new1[i, j]= temp[4] 

img_new1 = img_new1.astype(np.uint8) 
cv2.imshow('new_median_filtered.png', img_new1) 
cv2.waitKey(0)
cv2.destroyAllWindows()