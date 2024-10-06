import cv2
video = cv2.VideoCapture("my_video.mp4")

while True:
    success, frame = video.read()
    if not success:
        break
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, otsu_thresh = cv2.threshold(gray_frame, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    cv2.imshow("Original Frame", frame)
    cv2.imshow("Otsu Threshold Frame", otsu_thresh)
    
    if cv2.waitKey(50) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
