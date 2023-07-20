import numpy as np
import cv2
import face_recognition

imgKhang = face_recognition.load_image_file('OpenCV/img/z4533842960509_92f4ffbf7b11c54cbe5a2102aa643814.jpg')
imgKhang = cv2.cvtColor(imgKhang,cv2.COLOR_BGR2RGB)
imgKhangTest = face_recognition.load_image_file('OpenCV/img/z4533844284931_045324441d495d54fbdc91ddfec738cb.jpg')
imgKhangTest = cv2.cvtColor(imgKhangTest,cv2.COLOR_BGR2RGB)

faceLoc = face_recognition.face_locations(imgKhang)[0] #top right bottom left
print(faceLoc)
encodeKhang = face_recognition.face_encodings(imgKhang)[0]

faceLocTest = face_recognition.face_locations(imgKhangTest)[0] #top right bottom left
print(faceLocTest)
encodeKhangTest = face_recognition.face_encodings(imgKhangTest)[0]

cv2.rectangle(imgKhang,(faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255, 0 , 222), 5)
cv2.rectangle(imgKhangTest,(faceLocTest[3], faceLocTest[0]), (faceLocTest[1], faceLocTest[2]), (255, 0 , 255), 2)

results = face_recognition.compare_faces([encodeKhang],encodeKhangTest)
faceDis = face_recognition.face_distance([encodeKhang], encodeKhangTest)

cv2.putText(imgKhang, f'{results} {round(faceDis[0],2)}',(50,50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255),2)
print(results, faceDis)


cv2.imshow('Khang', imgKhang)
cv2.imshow('Khang Test', imgKhangTest)
cv2.waitKey(0)