import cv2
face_cascade = cv2.CascadeClassifier('trained_model/haarcascade_frontalface_default.xml')

cam = cv2.VideoCapture(0)

if not cam.isOpened():
    print("Error: Cannot access webcam")
    exit()

while True:
    # Read frame-by-frame
    ret, frame = cam.read()
    if not ret:
        print("Failed to grab frame")
        break

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5)

    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    
    cv2.putText(frame, "Press 'q' to quit", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 
                0.7, (255, 255, 255), 1)
    
    # Show result
    cv2.imshow('Face Detection - press q to quit', frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()