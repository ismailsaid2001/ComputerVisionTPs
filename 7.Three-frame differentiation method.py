import cv2
import numpy as np

# Open video file
video = cv2.VideoCapture("my_video.mp4")

# Read the first two frames and convert them to grayscale
_, frame1 = video.read()
_, frame2 = video.read()
gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

while True:
    success, frame3 = video.read()
    if not success:
        break
    
    # Convert the third frame to grayscale
    gray3 = cv2.cvtColor(frame3, cv2.COLOR_BGR2GRAY)
    
    # Compute the absolute differences between consecutive frames
    diff1 = cv2.absdiff(gray1, gray2)
    diff2 = cv2.absdiff(gray2, gray3)
    
    # Apply Otsu's thresholding to binarize the differences
    _, binarized_diff1 = cv2.threshold(diff1, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    _, binarized_diff2 = cv2.threshold(diff2, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # Perform logical AND operation (set to 255 where both binarized diffs are 255)
    combined_diff = np.logical_and(binarized_diff1 == 255, binarized_diff2 == 255).astype(np.uint8) * 255
    
    # Display the binarized three-frame difference
    cv2.imshow("Logical AND Three-frame Difference", combined_diff)
    
    # Shift the frames for the next iteration
    gray1, gray2 = gray2, gray3
    
    # Break the loop on 'q' key press
    if cv2.waitKey(50) & 0xFF == ord('q'):
        break

# Release video capture object and close all windows
video.release()
cv2.destroyAllWindows()
