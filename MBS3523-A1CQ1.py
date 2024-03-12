import serial
import cv2

ser = serial.Serial('COM6', 115200)

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    ret, frame = cap.read()

    if ser.in_waiting > 0:
        temperature = ser.readline().decode('utf-8').rstrip()

        cv2.putText(frame, f"Temperature: {temperature} degree C", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        cv2.imshow('Sensor Data', frame)

    cv2.imshow('Webcam', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()