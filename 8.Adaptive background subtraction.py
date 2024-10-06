import cv2
import numpy as np

# Create background subtractor
fgbg = cv2.createBackgroundSubtractorMOG2()

# Open video file
video = cv2.VideoCapture("my_video.mp4")

# Read the first frame
_, frame = video.read()
fgmask_prev = fgbg.apply(frame, learningRate=0.1)

while True:
    success, frame = video.read()
    if not success:
        break
    
    # Apply background subtraction
    fgmask_curr = fgbg.apply(frame, learningRate=0.1)
    
    # Binarize the current and previous foreground masks
    _, binarized_fgmask_prev = cv2.threshold(fgmask_prev, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    _, binarized_fgmask_curr = cv2.threshold(fgmask_curr, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # Perform logical AND operation between the current and previous frame masks
    combined_mask = np.logical_and(binarized_fgmask_prev == 255, binarized_fgmask_curr == 255).astype(np.uint8) * 255
    
    # Display the combined mask
    cv2.imshow("Logical AND Foreground Mask", combined_mask)
    
    # Update the previous mask for the next iteration
    fgmask_prev = fgmask_curr
    
    # Break the loop on 'q' key press
    if cv2.waitKey(50) & 0xFF == ord('q'):
        break

# Release video capture object and close all windows
video.release()
cv2.destroyAllWindows()
