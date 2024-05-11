import cv2


def detect_objects(image, config):
    # Load the object detection model
    net = cv2.dnn.readNetFromDarknet(config["model_config"], config["model_weights"])

    # Perform object detection on the image
    blob = cv2.dnn.blobFromImage(
        image, config["input_scale"], config["input_size"], config["mean_subtraction"]
    )
    net.setInput(blob)
    detections = net.forward()

    return detections
