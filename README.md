# Face Detection Attendance System

A Python-based attendance management system that uses face detection and face recognition to automate attendance marking. The system captures facial data through a webcam, trains a recognition model, identifies registered users in real time, and records attendance automatically.

## Features

* Student registration with face image capture
* Real-time face detection and recognition
* Automatic attendance marking
* Attendance report management
* CSV-based attendance storage
* Database integration
* Simple desktop GUI built with Tkinter

## Tech Stack

* Python
* OpenCV
* Tkinter
* NumPy
* SQLite / MySQL
* LBPH Face Recognition Algorithm

## Project Structure

```text
FaceDetectionAttendanceSystem/
│
├── assets/                      # Images, icons and UI resources
├── Attendance/                  # Attendance records and CSV files
├── dataset/                     # Captured face images
├── Training/                    # Trained model files
│
├── CaptureImages.py             # Capture and save face samples
├── FrameToImage.py              # Image processing utilities
├── Home.py                      # Main application interface
├── MarkAttendance.py            # Face recognition and attendance marking
├── ModelTraining.py             # Train face recognition model
├── ViewAttendance.py            # View attendance records
├── Variables.py                 # Shared variables and configuration
├── face_detection.sql           # Database schema
│
└── README.md
```

## Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/FaceDetectionAttendanceSystem.git
cd FaceDetectionAttendanceSystem
```

### Install Dependencies

```bash
pip install opencv-python numpy pillow
```

or

```bash
pip install -r requirements.txt
```

## Running the Project

### Launch the Main Application

```bash
python Home.py
```

### Register a Student

```bash
python CaptureImages.py
```

### Train the Recognition Model

```bash
python ModelTraining.py
```

### Mark Attendance

```bash
python MarkAttendance.py
```

### View Attendance Records

```bash
python ViewAttendance.py
```

## How It Works

1. Register a student by entering their details.
2. Capture multiple face samples using the webcam.
3. Store captured images in the dataset directory.
4. Train the LBPH face recognition model using the captured images.
5. Generate trained recognition data and save it in the Training directory.
6. Start the attendance module.
7. Detect and recognize faces in real time.
8. Automatically record attendance with date and time.
9. Store attendance records for later viewing and reporting.


## Screenshots

### Main Window

The central interface from which all major operations can be accessed.

<img width="1919" height="1012" alt="image" src="https://github.com/user-attachments/assets/ae95dc4e-8bf5-4a61-8944-deb039bf2796" />

---

### Student Registration

Register new students and capture facial data for training.

Register:

<img width="1919" height="1013" alt="image" src="https://github.com/user-attachments/assets/b14f8663-04ff-48bd-8b66-b6e9ff07180a" />

Facial data:

<img width="1874" height="839" alt="image" src="https://github.com/user-attachments/assets/27f27985-c946-4245-9828-d2e28b9190f7" />


---

### Attendance Marking

Marked Attendance popup.

<img width="1891" height="931" alt="image" src="https://github.com/user-attachments/assets/a5a92672-65cb-49dd-acc5-f7e1e6ea7bca" />


---

### Attendance Records

View and manage stored attendance records.
(attendance records are stored in csv files.)

<img width="643" height="309" alt="image" src="https://github.com/user-attachments/assets/810432f7-9a2f-4f7a-ae26-d87da6e09ff9" />


## Acknowledgements

This project uses:

* OpenCV for face detection and recognition
* Tkinter for the graphical user interface
* NumPy for numerical operations and image processing
