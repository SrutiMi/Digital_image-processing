# using functions 
# import cv2
# import numpy as np

# def apply_prewitt(image):
#     # Create a 3x3 kernel for Prewitt operator
#     kernel_x = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])
#     kernel_y = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])

#     # Apply the Prewitt operator
#     prewitt_x = cv2.filter2D(image, -1, kernel_x)
#     prewitt_y = cv2.filter2D(image, -1, kernel_y)

#     # Combine the results
#     prewitt = cv2.addWeighted(prewitt_x, 0.5, prewitt_y, 0.5, 0)

#     return prewitt

# # Read the image
# image = cv2.imread('image/download.jpeg', 0)
# cv2.imshow('new image',apply_prewitt(image))
# cv2.waitKey(0)

# without predefined functions
import cv2
import numpy as np

def apply_prewitt_operator(image):
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Create kernels for Prewitt Operator
    kernel_x = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
    kernel_y = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])

    # Get image dimensions
    height, width = gray_image.shape

    # Create an empty image to store the filtered result
    filtered_image = np.zeros((height, width), dtype=np.float32)

    # Iterate over each pixel in the image, excluding the border pixels
    for i in range(1, height - 1):
        for j in range(1, width - 1):
            # Apply the kernel to the neighborhood of each pixel
            gradient_x = np.sum(gray_image[i - 1:i + 2, j - 1:j + 2] * kernel_x)
            gradient_y = np.sum(gray_image[i - 1:i + 2, j - 1:j + 2] * kernel_y)
            
            # Calculate the magnitude of the gradient
            magnitude = np.sqrt(gradient_x**2 + gradient_y**2)
            filtered_image[i, j] = magnitude

    # Normalize the filtered image to the range [0, 255]
    filtered_image = (filtered_image / np.max(filtered_image)) * 255
    filtered_image = np.uint8(filtered_image)

    return filtered_image

def display_image(image, window_name):
    cv2.imshow(window_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    # Read the input image
    img = cv2.imread('image/download.jpeg')

    # Apply the Prewitt Operator for edge detection
    edge_result = apply_prewitt_operator(img)

    # Display the original and edge-detected images
    display_image(img, 'Original Image')
    display_image(edge_result, 'Edge Detection using Prewitt Operator')

if __name__ == "__main__":
    main()

