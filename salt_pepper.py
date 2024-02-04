import cv2
import numpy as np

def apply_median_filter(image):
    m, n = image.shape
    img_new = np.zeros([m, n], dtype=np.uint8)

    for i in range(1, m-1):
        for j in range(1, n-1):
            temp = [image[i-1, j-1],
                    image[i-1, j],
                    image[i-1, j + 1],
                    image[i, j-1],
                    image[i, j],
                    image[i, j + 1],
                    image[i + 1, j-1],
                    image[i + 1, j],
                    image[i + 1, j + 1]]

            temp = sorted(temp)
            img_new[i, j] = temp[4]

    return img_new

def add_salt_and_pepper_noise(image, salt_prob, pepper_prob):
    noisy_image = np.copy(image)
    total_pixels = image.size

    # Add salt noise
    num_salt = np.ceil(salt_prob * total_pixels)
    salt_coords = [np.random.randint(0, i - 1, int(num_salt)) for i in image.shape]
    noisy_image[salt_coords[0], salt_coords[1]] = 255

    # Add pepper noise
    num_pepper = np.ceil(pepper_prob * total_pixels)
    pepper_coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in image.shape]
    noisy_image[pepper_coords[0], pepper_coords[1]] = 0

    return noisy_image

def display_image(image, title):
    cv2.imshow(title, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Read the grayscale image
path = 'image/3.jpg'
original_image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

if original_image is not None:
    # Add salt and pepper noise
    salt_and_pepper_noisy_image = add_salt_and_pepper_noise(original_image, salt_prob=0.02, pepper_prob=0.02)

    # Display the original and noisy images
    display_image(original_image, 'Original Image')
    display_image(salt_and_pepper_noisy_image, 'Salt and Pepper Noisy Image')
    # filtered image
    display_image(apply_median_filter(salt_and_pepper_noisy_image), 'Median Filtered Image')

    
else:
    print("Error: Unable to read the image.")