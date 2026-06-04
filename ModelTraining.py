import cv2
import os
import numpy as np
from tkinter import messagebox
import Variables as V
def train_model():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    trainer_path = V.trainer_path
    path = V.path
    image_paths = [os.path.join(path, f) for f in os.listdir(path)]
    face_samples, ids = [], []

    for image_path in image_paths:
        img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        # Extract Roll Number from filename: User.RollNo.Sample.jpg
        student_id = int(os.path.split(image_path)[-1].split(".")[1])
        student_name = os.path.split(image_path)[-1].split(".")[0]
        face_samples.append(img)
        ids.append(student_id)

    recognizer.train(face_samples, np.array(ids))
    recognizer.save(trainer_path)
    # messagebox.showinfo("Success", "Registration Successful.")