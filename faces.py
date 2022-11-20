import urllib
import numpy as np
import mysql.connector
import cv2
import pyttsx3
import pickle
from datetime import datetime
import sys

myconn = mysql.connector.connect(host="localhost", user="root", passwd="sz123wwl", database="gp")

def run():
    # timer
    time = 0
    
    # 1 Create database connection
    date = datetime.utcnow()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    global myconn
    cursor = myconn.cursor()

    #2 Load recognize and read label from model
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("train.yml")

    labels = {"person_name": 1}
    with open("labels.pickle", "rb") as f:
        labels = pickle.load(f)
        labels = {v: k for k, v in labels.items()}

    # create text to speech
    engine = pyttsx3.init()
    rate = engine.getProperty("rate")
    engine.setProperty("rate", 175)

    # Define camera and detect face
    face_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)

    # result
    find = 0
    userID_found = 0

    # 3 Open the camera and start face recognition
    while True:
        time += 1
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

        for (x, y, w, h) in faces:
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]
            # predict the id and confidence for faces
            id_, conf = recognizer.predict(roi_gray)

            # If the face is recognized
            if conf >= 60:
                # print(id_)
                # print(labels[id_])
                font = cv2.QT_FONT_NORMAL
                id = 0
                id += 1
                name = labels[id_]
                current_name = name
                color = (255, 0, 0)
                stroke = 2
                cv2.putText(frame, name, (x, y), font, 1, color, stroke, cv2.LINE_AA)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), (2))

                # Find the student's information in the database.
                select = "SELECT userID, userName, DAY(login_date), MONTH(login_date), YEAR(login_date) FROM UserInfo WHERE userName = '%s'" % (name)
                name = cursor.execute(select)
                result = cursor.fetchall()
                # print(result)
                data = "error"

                for x in result:
                    data = x

                # If the student's information is not found in the database
                if data == "error":
                    print("The student", current_name, "is NOT FOUND in the database.")

                # If the student's information is found in the database
                else:
                    find = 1
                    select = "SELECT userID FROM UserInfo WHERE userName = '%s'" % (current_name)
                    cursor.execute(select)
                    result = cursor.fetchall()
                    userID_found = result[0][0]
                    # Update the data in database
                    update =  "UPDATE UserInfo SET login_date = %s WHERE userName = %s"
                    val = (date, current_name)
                    cursor.execute(update, val)
                    update =  "UPDATE UserInfo SET login_time = %s WHERE userName = %s"
                    val = (current_time, current_name)
                    cursor.execute(update, val)
                    myconn.commit()
               
                    hello = ("Hello ", current_name, "You did attendance today")
                    #print(hello)
                    engine.say(hello)
                    # engine.runAndWait()


            # If the face is unrecognized
            else: 
                color = (255, 0, 0)
                stroke = 2
                font = cv2.QT_FONT_NORMAL
                cv2.putText(frame, "UNKNOWN", (x, y), font, 1, color, stroke, cv2.LINE_AA)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), (2))
                hello = ("Your face is not recognized")
                #print(hello)
                engine.say(hello)
                # engine.runAndWait()

        cv2.imshow('Login with face', frame)
    
        k = cv2.waitKey(20) & 0xff
        if k == ord('q'):
            break
    
        if find == 1 or time == 300:
            break
        
    cap.release()
    cv2.destroyAllWindows()
    return userID_found
