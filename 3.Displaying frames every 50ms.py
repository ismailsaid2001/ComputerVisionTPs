import cv2
video = cv2.VideoCapture("my_video.mp4")

while True:
    success, frame = video.read()
    if not success:
        break
    cv2.imshow("Video Frame", frame)
    if cv2.waitKey(50) & 0xFF == ord('q'):  # Display each frame every 50ms
        break

video.release()
cv2.destroyAllWindows()
