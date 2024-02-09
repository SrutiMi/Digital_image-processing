# with function
import cv2
import numpy as np

def apply_robert(image):
    kernel_x = np.array([[1,0],[0,-1]])
    kernel_y = np.array([[0,1],[-1,0]])

    sobel_x = cv2.filter2D(image,-1,kernel_x)
    sobel_y = cv2.filter2D(image,-1,kernel_y)

    sobel = cv2.addWeighted(sobel_x,0.5,sobel_y,0.5,0)
    return sobel

image = cv2.imread('image\download.jpeg',0)
cv2.imshow('New',apply_robert(image))
cv2.waitKey(0)
# _____________________________

# without predefined functions
# import cv2
# import numpy as np

# def apply_robert(image):
#     # defining the kernels
#     kernel_x = np.array([[1,0], [0,-1]])
#     kernel_y = np.array([[0,1],[-1,0]])

#     height,width = image.shape
#     # creating an empty image
#     filter_image = np.zeros((height, width), dtype=np.float32)

#     # iterating over the pixel values except the border
#     for i in range(0, height - 1):
#         for j in range(0, width - 1):
#             # calculating gradients along x and y
#             gradient_x = np.sum(image[i:i + 2, j:j + 2] * kernel_x)
#             gradient_y = np.sum(image[i :i + 2, j :j + 2] * kernel_y)

#             magnitude = np.sqrt(gradient_x ** 2 + gradient_y ** 2)
#             filter_image[i, j] = magnitude

#     # normalizing
#     filter_image = (filter_image / np.max(filter_image)) * 255
#     filter_image = np.uint8(filter_image)
#     return filter_image

# image = cv2.imread('image\download.jpeg', 0)
# cv2.imshow('New', apply_robert(image))
# cv2.waitKey(0)
# cv2.destroyAllWindows()