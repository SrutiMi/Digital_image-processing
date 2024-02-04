import cv2
import numpy as np

def power_law_transformation(image, gamma):
    # Power-Law (Gamma) Transformation: s = c * r^gamma
    c= 255 # Scaling factor for normalization to 0-255 range
    r=image.astype(float)
    power_law_transformed_image = c * (r/255 )** gamma
    return power_law_transformed_image.astype('uint8')  # Convert to uint8

def image_subtraction(original_image, enhanced_image):
    # Image Subtraction: Subtract the original image from the enhanced image
    subtracted_image = np.abs(enhanced_image - original_image)
    return subtracted_image.astype('uint8')  # Convert to uint8

def display_image(image, title):
    # Display the image using OpenCV
    cv2.imshow(title, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Read the grayscale image
original_image = cv2.imread('image/3.jpg', cv2.IMREAD_GRAYSCALE)

if original_image is not None:
    # Display the original image
    display_image(original_image, 'Original Image')

    # Power-Law (Gamma) Transformation
    gamma_value = float(input("Enter gamma value (e.g., 0.5 for darker, 2.0 for brighter): "))
    enhanced_image = power_law_transformation(original_image, gamma_value)
    display_image(enhanced_image, 'Enhanced Image (Power Law Transformation)')

    # Image Subtraction
    subtracted_image = image_subtraction(original_image, enhanced_image)
    display_image(subtracted_image, 'Image Subtraction (Enhanced - Original)')

else:
    print("Error: Unable to read the image.")
