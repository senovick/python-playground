import cv2, time

first_frame = None

video = cv2.VideoCapture("sample.mp4")

while True:
    ret, frame = video.read()
    if frame is None:
        break
    resized = cv2.resize(frame, (800, 600))
    cv2.imshow("Video Capture", resized)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break
video.release()
cv2.destroyAllWindows
