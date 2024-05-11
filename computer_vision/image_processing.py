import cv2

def process_image(image, config):
    # Perform image processing using the specified configuration
    # For example, apply a filter or transform the image

    # Apply a filter
    filtered_image = cv2.GaussianBlur(image, (config['filter_size'], config['filter_size']), config['filter_sigma'])

    return filtered_image
