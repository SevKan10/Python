import numpy as np
import cv2
import dlib

# Load the image
imgThongBig = cv2.imread('ImageBasic/khang.jpg')

# Convert the image to grayscale for face detection
gray = cv2.cvtColor(imgThongBig, cv2.COLOR_BGR2GRAY)

# Initialize a face detector from dlib
detector = dlib.get_frontal_face_detector()

# Detect faces in the image
faces = detector(gray)

# Loop through the detected faces
for face in faces:
    x, y, w, h = face.left(), face.top(), face.width(), face.height()

    # Draw a rectangle around each detected face
    cv2.rectangle(imgThongBig, (x, y), (x + w, y + h), (255, 0, 222), 5)

# Display the image with detected faces
cv2.imshow('Thong Big', imgThongBig)
cv2.waitKey(0)
cv2.destroyAllWindows()
