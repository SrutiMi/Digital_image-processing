import cv2
import numpy as np

def rotate_image_custom(image, angle):
    # Convert the angle to radians
    angle_rad = np.radians(angle)

    # Get image dimensions
    rows, cols = image.shape[:2]

    # Calculate the rotation matrix
    cos_val = np.cos(angle_rad)
    sin_val = np.sin(angle_rad)
    rotation_matrix = np.array([[cos_val, -sin_val],
                                [sin_val, cos_val]])

    # Find the new image dimensions after rotation
    new_cols = int(cols * np.abs(cos_val) + rows * np.abs(sin_val))
    new_rows = int(rows * np.abs(cos_val) + cols * np.abs(sin_val))

    # Create an empty image with the new dimensions
    rotated_image = np.zeros((new_rows, new_cols, 3), dtype=np.uint8)

    # Find the translation components to center the rotated image
    tx = (new_cols - cols) // 2
    ty = (new_rows - rows) // 2

    # Iterate through the original image pixels
    for i in range(rows):
        for j in range(cols):
            # Apply the rotation matrix to find the new coordinates
            new_coords = np.dot(rotation_matrix, np.array([j - cols//2, i - rows//2]))
            new_coords = np.round(new_coords).astype(int)

            # Offset the new coordinates to center the rotated image
            new_coords[0] += new_cols // 2
            new_coords[1] += new_rows // 2

            # Check if the new coordinates are within bounds
            if 0 <= new_coords[0] < new_cols and 0 <= new_coords[1] < new_rows:
                # Copy the pixel value to the rotated image
                rotated_image[new_coords[1], new_coords[0]] = image[i, j]

    return rotated_image

# path
path = 'image/gfg.png'

# Reading an image in default mode
src = cv2.imread(path)

# Window name in which image is displayed
window_name = 'Image'

# Manually rotate the image by 45 degrees
rotated_image = rotate_image_custom(src, 45)

# Displaying the image
cv2.imshow(window_name, rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
