from base64 import encode
import cv2
import numpy as np
import face_recognition

imgElon=face_recognition.load_image_file("image/Elon_Musk.jpg")
imgElon=cv2.cvtColor(imgElon,cv2.COLOR_BGR2RGB)
imgTest=face_recognition.load_image_file("image/Bill.jpg")
imgTest=cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)

faceLoc=face_recognition.face_locations(imgElon)[0]
encodeElon=face_recognition.face_encodings(imgElon)[0]
cv2.rectangle(imgElon,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,0,240),2)

faceLoctest=face_recognition.face_locations(imgTest)[0]
encodetest=face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest,(faceLoctest[3],faceLoctest[0]),(faceLoctest[1],faceLoctest[2]),(255,0,240),2)

result=face_recognition.compare_faces([encodeElon],encodetest)
print(result)

cv2.imshow('Elon_Musk',imgElon)
cv2.imshow('Elon_test',imgTest)
cv2.waitKey(0)