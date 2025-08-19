# Face-Detection-App with OpenCV
This is a basic real-time face detection script using Python and OpenCV. It accesses the webcam, detects faces using a pre-trained Haar Cascade model, and displays the video feed with rectangles around detected faces.

## 📌Features
- Real-time face detection from webcam
- Uses Haar Cascade Classifier (haarcascade_frontalface_default.xml)
- Simple and lightweight implementation
- Press q to exit the video stream

## 🧰Prerequisites
- Python 3.x
- OpenCV library

## 🔧Installation
- Clone the repository (if applicable) or download the script.
- Install OpenCV: pip install opencv-python
- Ensure you have the Haar Cascade XML file:
- Download haarcascade_frontalface_default.xml from OpenCV’s GitHub: https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
- Save it to a folder named trained_model/ in the same directory as the script.

## ▶️Usage
- Run the script
- Once the webcam opens:
- A window will display your video feed.
- Detected faces will be marked with green rectangles.
- Press q to quit.

## 📁File Structure
```
project_folder/
│
├── main.py
└── trained_model/
    └── haarcascade_frontalface_default.xml
```

## 📝Notes
Ensure your webcam is accessible and not being used by another application.
You can adjust scaleFactor and minNeighbors in detectMultiScale() to tweak detection sensitivity.

## 📄License
This project is open source and free to use for educational purposes.
