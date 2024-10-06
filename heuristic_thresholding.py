import cv2
import numpy as np

def heuristic_thresholding(gray_frame, initial_threshold):
    T = initial_threshold
    while True:
        # Segmentation: pixels above threshold are foreground, others background
        foreground = gray_frame[gray_frame > T]
        background = gray_frame[gray_frame <= T]
        
        # Calculate means of foreground and background
        mean_foreground = np.mean(foreground) if len(foreground) > 0 else 0
        mean_background = np.mean(background) if len(background) > 0 else 0
        
        # Calculate new threshold
        new_T = (mean_foreground + mean_background) / 2
        
        # Stop if the threshold stabilizes
        if abs(new_T - T) < 1:  # You can adjust the threshold for convergence
            break
        
        T = new_T  # Update threshold
        
    return T

# Load the video
video = cv2.VideoCapture("my_video.mp4")

# Read a specific frame (for example, the first frame)
success, frame = video.read()
if not success:
    print("Failed to read the video.")
    video.release()
    exit()

# Convert to grayscale
gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Choose different initial thresholds to test
initial_thresholds = [50, 100, 150, 200]

for T_init in initial_thresholds:
    # Apply heuristic thresholding
    final_threshold = heuristic_thresholding(gray_frame, T_init)
    
    # Thresholding the image using the final threshold
    _, thresholded_frame = cv2.threshold(gray_frame, final_threshold, 255, cv2.THRESH_BINARY)

    # Display the results
    cv2.imshow(f'Original Frame', frame)
    cv2.imshow(f'Thresholded Frame (Init T={T_init}, Final T={final_threshold:.2f})', thresholded_frame)
    print(final_threshold)
    cv2.waitKey(0)

# Release resources
video.release()
cv2.destroyAllWindows()
