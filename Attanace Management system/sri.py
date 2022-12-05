from base64 import encode
from pydoc import classname
from unicodedata import name
import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
import exel

path='image'
image=[]
classNames=[]
myList=os.listdir(path)
#print(myList)

for i in myList:
    curImg=cv2.imread(f'{path}/{i}')
    image.append(curImg)
    classNames.append(os.path.splitext(i)[0])

#print(classNames)
def findEncodings(image):
    encodeList=[]
    for img in image:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode=face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

encodeListKnown=findEncodings(image)

presentlist=[]
presentlist2=[]
#cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
def relist():
    exel.writting(presentlist)
    

def fuck():
 cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
 f=1
 while True:
    success, img = cap.read()
    imgS = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB) 
    
    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)
    

    for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name=classNames[matchIndex].upper()
            #print(name)
            y1,x2,y2,x1 = faceLoc
            y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            if name not in presentlist2:
                presentlist2.append(name)
                presentlist.append([name,str(datetime.now())])

            if len(presentlist2)==3:
                f=0
                break
    if f==0:
        break 
    cv2.imshow('Webcam',img)
    cv2.waitKey(1)
            #cv2.imshow('Webcam',img)
    #        if name not in presentlist:
    #            presentlist.append(name)
    #    if len(presentlist)==3:
    #        f=0
    #        break
   # print(presentlist)
    #if f==0:
    #    break 
    
    


if __name__=='__main__':
    fuck()
    relist()        
#print(presentlist)
        
    


            

