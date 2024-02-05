import cv2

print(cv2.__version__)


cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)


cv2.namedWindow("Webcam Frames", cv2.WINDOW_NORMAL)

while True:
    success, frame = cam.read()

    if not success:
        print("Failed to capture frame")
        break


    frame_flip_horizontal = cv2.flip(frame, 1)
    frame_flip_vertical = cv2.flip(frame, 0)
    frame_flip_both = cv2.flip(frame, -1)

    canvas_top = cv2.hconcat([frame, frame_flip_horizontal])
    canvas_bottom = cv2.hconcat([frame_flip_vertical, frame_flip_both])

    canvas = cv2.vconcat([canvas_top, canvas_bottom])

    cv2.imshow("Webcam Frames", canvas)

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()