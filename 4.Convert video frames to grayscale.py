import cv2
video = cv2.VideoCapture("my_video.mp4")

while True:
    success, frame = video.read()
    if not success:
        break
    # Convert to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Grayscale Frame", gray_frame)
    
    if cv2.waitKey(50) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
