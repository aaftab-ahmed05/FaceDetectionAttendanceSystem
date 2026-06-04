import cv2
from tkinter import messagebox
import os
import Variables as V

dataset_path = V.path
if not os.path.exists(dataset_path):
    os.makedirs(dataset_path)

def capture_image(roll,name):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    cap = cv2.VideoCapture(0)
    count = 0
    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            count += 1
            # Save grayscale face for LBPH training
            cv2.imwrite(f"{dataset_path}/{name}.{roll}.{count}.jpg", gray[y:y + h, x:x + w])
            cv2.rectangle(frame, (x, y), (x + w, y + h), (68, 24, 129), 2)

        cv2.imshow("Registering...", frame)
        cv2.moveWindow("Registering...", 600, 100)
        if cv2.waitKey(1) & 0xFF == ord('q') or count >= 30:
            break

    cap.release()
    cv2.destroyAllWindows()
    messagebox.showinfo("Success", f"Captured 30 samples.")
    V.capture_flag = True