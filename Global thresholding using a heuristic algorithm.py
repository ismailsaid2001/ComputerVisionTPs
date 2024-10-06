import numpy as np
import cv2

# Heuristic thresholding function to calculate an adaptive threshold
def heuristic_thresholding(gray_frame, initial_threshold):
    T = initial_threshold
    while True:
        # Segmentation: pixels above threshold are foreground, others background
        foreground = gray_frame[gray_frame > T]
        background = gray_frame[gray_frame <= T]
        
        # Recalculate threshold
        new_T = (np.mean(foreground) + np.mean(background)) / 2
        
        # Stop if threshold stabilizes
        if abs(new_T - T) < 1:
            break
        T = new_T
    return T

# Load video and process the first frame
video = cv2.VideoCapture("my_video.mp4")
_, frame = video.read()

# Convert the frame to grayscale
gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Apply heuristic thresholding to determine the optimal threshold
threshold = heuristic_thresholding(gray_frame, 128)  # Initial threshold 128

# Binarize the image using the calculated threshold
_, thresholded_frame = cv2.threshold(gray_frame, threshold, 255, cv2.THRESH_BINARY)

# Display the thresholded (binarized) frame
cv2.imshow("Thresholded Frame", thresholded_frame)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Release video resources
video.release()
