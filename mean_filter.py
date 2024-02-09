import cv2
import numpy as np

def mean_filter(image, kernel):

  height,width=image.shape[:2]
  image = cv2.copyMakeBorder(image,kernel//2,kernel//2,kernel//2,kernel//2,cv2.BORDER_CONSTANT)

  result=np.zeros_like(image,dtype=np.float32)
  for i in range(kernel//2,height-kernel//2):
    for j in range(kernel//2,width-kernel//2):
      result[i,j]=np.mean(image[i-kernel//2:i+kernel//2+1,j-kernel//2:j+kernel//2+1])
  result=result.astype(np.uint8)
  cv2.imshow("Output",result)
  cv2.waitKey(0)

img = cv2.imread('image/filter.png')
mean_filter(img,3)
