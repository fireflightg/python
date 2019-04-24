# python track.py
import numpy as np
import cv2
from firebase import firebase
from firebase_admin import db
facecass = cv2.CascadeClassifier('data/myhaar.xml')
facecase = cv2.CascadeClassifier('myhaar.xml')
firebase = firebase.FirebaseApplication('https://smrtgarder.firebaseio.com/')
#webcam = cv2.VideoCapture("http://underdon-chihuahua-1038.dataplicity.io/")
webcam = cv2.VideoCapture("http://192.168.0.141:8080/video")

while True:
   rect, frame = webcam.read()

   gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   face = facecass.detectMultiScale(gray, scaleFactor=1.5, minNeighbors= 5)
   for (x,y,w,h) in face:

      print(x,y,w,h)
      result = firebase.put('plant','cool',{"2": 2})
      roi_gray = gray[y:y+h, x:x+w]
      roi_color = frame[y:y+h, x:x+w]
      img_item = "faceimgfromdetection.png"
      cv2.imwrite(img_item, roi_color)

      color = (255,0,0) #BGR
      stroke = 2
      wid = x + w
      hit = y + h 
      cv2.rectangle(frame, (x,y), (wid,hit), color, stroke) #(x,y) stand for starting coords and wid and hit stand for end coords
   faced = facecase.detectMultiScale(gray, scaleFactor=1.5, minNeighbors= 5)
   for (x,y,w,h) in faced:
      print(x,y,w,h)
      xx = x
      xxx = (x,y,w,h)

      result = firebase.put('plant','cool',{"1": 1})

      roi_gray = gray[y:y+h, x:x+w]
      roi_color = frame[y:y+h, x:x+w]
      img_item = "faceimgfromdetection.png"
      cv2.imwrite(img_item, roi_color)

      color = (0,0,255) #BGR
      stroke = 2
      wid = x + w
      hit = y + h 
      cv2.rectangle(frame, (x,y), (wid,hit), color, stroke)
      


   cv2.imshow('frame', frame)
   cv2.imshow('frame2', gray)
   if cv2.waitKey(20) & 0xFF == ord('q'):
         break  
