import cv2
from PIL import Image, ImageTk

def frame_to_image(frame):
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = Image.fromarray(frame)
        img = ImageTk.PhotoImage(image=frame)
        return img
