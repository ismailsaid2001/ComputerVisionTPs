import cv2

# Open video file
video = cv2.VideoCapture("my_video.mp4")

# Read the first frame and convert it to grayscale
success, previous_frame = video.read()
if not success:
    print("Error: Could not read video file.")
    exit()

previous_gray = cv2.cvtColor(previous_frame, cv2.COLOR_BGR2GRAY)

while True:
    success, frame = video.read()
    if not success:
        break
    
    # Convert the current frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Compute the absolute difference between the previous and current grayscale frames
    frame_diff = cv2.absdiff(previous_gray, gray_frame)
    
    # Apply Otsu's thresholding to binarize the frame difference
    _, binarized_diff = cv2.threshold(frame_diff, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # Display the binarized frame difference
    cv2.imshow("Binarized Frame Difference", binarized_diff)
    
    # Update the previous frame
    previous_gray = gray_frame
    
    # Break the loop on 'q' key press
    if cv2.waitKey(50) & 0xFF == ord('q'):
        break

# Release video capture object and close all windows
video.release()
cv2.destroyAllWindows()
