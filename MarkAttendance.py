import cv2
from tkinter import messagebox
import os
from datetime import datetime
import Variables as V
import pandas as pd
import pymysql


try:
    conn = pymysql.connect(host=V.host, user=V.user, password=V.password, database=V.database)
    curr = conn.cursor()
except Exception as e:
        messagebox.showerror("Database Error", "Error while connecting to the database :\n" + str(e))

def mark_attendance():

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    trainer_path = V.trainer_path
    path = V.path
    if not os.path.exists(trainer_path):
        messagebox.showerror("Error", "No Data found.")
        return

    recognizer.read(trainer_path)
    cap = cv2.VideoCapture(0)
    recognized_id = None
    name = None

    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.2, 5)

        for (x, y, w, h) in faces:
            id, confidence = recognizer.predict(gray[y:y + h, x:x + w])
            cv2.rectangle(frame, (x, y), (x + w, y + h), (68, 24, 129), 2)

            # Confidence 0 is a perfect match for LBPH
            if confidence < 55:
                recognized_id = id
                curr.execute("select name from students where roll=%s;", (id))
                name = curr.fetchone()[0]
                log_to_csv(recognized_id,name)
                break


        cv2.imshow("Scanning Attendance", frame)
        cv2.moveWindow("Scanning Attendance", 600,100)

        if recognized_id or name or (cv2.waitKey(1) & 0xFF == ord('q')):
            break

    cap.release()
    cv2.destroyAllWindows()
    if recognized_id:
        messagebox.showinfo("Success", f"Attendance Marked for {name} roll number {recognized_id}")

def log_to_csv(roll_no,name):
    if not os.path.exists("Attendance"):
        os.mkdir("Attendance")
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    file_name = f"Attendance/Attendance_{date_str}.csv"
    entry = pd.DataFrame({"Roll No.": [roll_no],"Name":[name],"Time": [now.strftime("%H:%M:%S")]})
    entry.to_csv(file_name, mode='a', header=not os.path.exists(file_name), index=False)