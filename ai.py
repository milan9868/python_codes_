import cv2
import numpy as np

# Define the golden ratio
golden_ratio = 1.61803398875

# Start the camera
camera = cv2.VideoCapture(0)

while True:
    # Capture a frame from the camera
    ret, frame = camera.read()

    # Convert the frame to grayscale and apply a face detection algorithm
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = cv2.CascadeClassifier('haarcascade_frontalface_default.xml').detectMultiScale(gray, 1.3, 5)

    # Loop through the detected faces
    for (x, y, w, h) in faces:
        # Calculate the width-to-height ratio of the face
        ratio = w / h

        # If the ratio is close to the golden ratio, draw a green rectangle around the face
        if abs(ratio - golden_ratio) < 0.1:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, 'Golden ratio', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        # Otherwise, draw a red rectangle around the face
        else:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
            cv2.putText(frame, 'Not golden ratio', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    # Display the frame with the overlaid rectangles
    cv2.imshow('Frame', frame)

    # Wait for the user to press a key
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

# Release the camera and close all windows
camera.release()
cv2.destroyAllWindows()
