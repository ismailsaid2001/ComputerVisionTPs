import os
import cv2
video = cv2.VideoCapture("my_video.mp4")

# Ensure output directory exists
if not os.path.exists("frames"):
    os.makedirs("frames")

# Read and save frames
frame_id = 0
while True:
    success, frame = video.read()
    if not success:
        break
    # Save every frame to the directory
    cv2.imwrite(f"frames/frame_{frame_id}.jpg", frame)
    frame_id += 1
video.release()
