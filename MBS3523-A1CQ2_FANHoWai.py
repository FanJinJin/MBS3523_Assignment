import cv2
import numpy as np
import serial

arduino = serial.Serial('COM6', 115200)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_color = np.array([0, 100, 100])
    upper_color = np.array([10, 255, 255])

    color_mask = cv2.inRange(hsv_frame, lower_color, upper_color)

    contours, _ = cv2.findContours(color_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) > 0:
        largest_contour = max(contours, key=cv2.contourArea)

        M = cv2.moments(largest_contour)
        if M['m00'] != 0:
            centroid_x = int(M['m10'] / M['m00'])
            centroid_y = int(M['m01'] / M['m00'])

            angle1 = np.interp(centroid_x, [0, frame.shape[1]], [0, 60])
            angle2 = np.interp(centroid_y, [0, frame.shape[0]], [0, 60])

            angle1 = np.clip(angle1, 0, 50)
            angle2 = np.clip(angle2, 00, 50)

            arduino.write(f"{int(angle1)} {int(angle2)}\n".encode())

    cv2.imshow('Color Tracking', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()