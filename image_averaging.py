import cv2
import numpy as np

def resize_image(image, target_shape):
    return cv2.resize(image, target_shape)

def average_images(image1, image2):
    # Resize images if they have different dimensions
    if image1.shape != image2.shape:
        target_shape = (max(image1.shape[0], image2.shape[0]), max(image1.shape[1], image2.shape[1]))
        image1 = resize_image(image1, target_shape)
        image2 = resize_image(image2, target_shape)

    return (image1 + image2) // 2

def display_image(image, title):
    cv2.imshow(title, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Read the first image
path_image1 = 'image/3.jpg'
image1 = cv2.imread(path_image1)

# Read the second image
path_image2 = 'image/gfg.png'
image2 = cv2.imread(path_image2)

if image1 is not None and image2 is not None:
    # Average the two images
    averaged_image = average_images(image1, image2)

    # Display the original images
    display_image(image1, 'Image 1')
    display_image(image2, 'Image 2')

    # Display the averaged image
    display_image(averaged_image, 'Averaged Image')

else:
    print("Error: Unable to read one or both of the images.")
