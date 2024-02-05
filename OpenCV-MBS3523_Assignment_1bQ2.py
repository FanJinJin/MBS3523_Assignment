import cv2
print(cv2.__version__)

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    success, frame = cam.read()
    frame = cv2.flip(frame, 1)


    frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    cv2.imshow('Original', frame)

    camblur = cv2.GaussianBlur(frame, (11, 11), 0)
    cv2.imshow('Gaussian Blur', camblur)

    camhsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    cv2.imshow('HSV', camhsv)

    camedges = cv2.Canny(frame, 100, 200)
    cv2.imshow('Canny Edges', camedges)

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()