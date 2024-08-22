import numpy as np
import cv2
import face_recognition

imgThongBig = face_recognition.load_image_file('ImageBasic\Duong Lam.jpg')
imgThongBig = cv2.cvtColor(imgThongBig,cv2.COLOR_BGR2RGB)
imgThongTest = face_recognition.load_image_file('ImageBasic/khang.jpg')
imgThongTest = cv2.cvtColor(imgThongTest,cv2.COLOR_BGR2RGB)

faceLoc = face_recognition.face_locations(imgThongBig)[0] #top right bottom left
print(faceLoc)
encodeThong = face_recognition.face_encodings(imgThongBig)[0]

faceLocTest = face_recognition.face_locations(imgThongTest)[0] #top right bottom left
print(faceLocTest)
encodeThongTest = face_recognition.face_encodings(imgThongTest)[0]

cv2.rectangle(imgThongBig,(faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255, 0 , 222), 5)
cv2.rectangle(imgThongTest,(faceLocTest[3], faceLocTest[0]), (faceLocTest[1], faceLocTest[2]), (255, 0 , 255), 2)

results = face_recognition.compare_faces([encodeThong],encodeThongTest)
faceDis = face_recognition.face_distance([encodeThong], encodeThongTest)

cv2.putText(imgThongBig, f'{results} {round(faceDis[0],2)}',(50,50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255),2)
print(results, faceDis)


cv2.imshow('Khang', imgThongBig)
cv2.imshow('Khang', imgThongTest)
cv2.waitKey(0)