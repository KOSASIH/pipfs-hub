import cv2


def process_video(video_path, config):
    # Perform video processing using the specified configuration
    # For example, extract frames or apply a filter

    # Extract frames
    cap = cv2.VideoCapture(video_path)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_rate = cap.get(cv2.CAP_PROP_FPS)
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    for i in range(frame_count):
        ret, frame = cap.read()
        if not ret:
            break

        # Apply a filter
        filtered_frame = cv2.GaussianBlur(
            frame,
            (config["filter_size"], config["filter_size"]),
            config["filter_sigma"],
        )

        # Write the filtered frame to a new video file
        out = cv2.VideoWriter(
            "filtered_" + video_path,
            cv2.VideoWriter_fourcc(*"XVID"),
            frame_rate,
            (frame_width, frame_height),
        )
        out.write(filtered_frame)
        out.release()

    cap.release()
