import cv2

# Load video
video = cv2.VideoCapture("my_video.mp4")

# Get video information
width = video.get(cv2.CAP_PROP_FRAME_WIDTH)
height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = video.get(cv2.CAP_PROP_FPS)
frame_count = video.get(cv2.CAP_PROP_FRAME_COUNT)

print(f"Width: {width}, Height: {height}, FPS: {fps}, Frame Count: {frame_count}")
