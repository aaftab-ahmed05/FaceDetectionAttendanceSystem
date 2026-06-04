from datetime import datetime
import os
from tkinter import messagebox


def view_logs():
    date_str = datetime.now().strftime("%Y-%m-%d")
    file_name = f"Attendance_{date_str}.csv"

    file_path = os.path.join("Attendance", file_name)

    if os.path.exists(file_path):
        os.startfile(file_path)
    else:
        messagebox.showwarning("File Not Found", "Today's attendance file does not exist.")