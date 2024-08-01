#Necessary Packages

import cv2
import sqlite3

faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')  # Detect faces in webcam
cam = cv2.VideoCapture(0)


def insertorupdate(id, name, age):
    conn=sqlite3.connect("sqlite.db")
    cmd="SELECT * FROM STUDENTS WHERE ID="+str(id)
    cursor = conn.execute(cmd)
    isRecordExist = 0
    for row in cursor:
        isRecordExist = 1
    if isRecordExist == 1:
        conn.execute("UPDATE STUDENTS SET NAME=? WHERE ID=?", (name, id))
        conn.execute("UPDATE STUDENTS SET age=? WHERE ID=?", (age, id))
    else:
        conn.execute("INSERT INTO STUDENTS (id,name,age) values(?,?,?)", (id, name, age))
    conn.commit()
    conn.close()


# insert userdefined values into table

Id = input("Enter user id: ")
name = input("Enter the user name: ")
age = input("Enter the user age: ")

insertorupdate(Id, name, age)

#detect face in web cam coding

samplenum = 0
while (True):
    ret, img = cam.read()
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(grey, 1.3, 5)
    for (x, y, w, h) in faces:
        samplenum = samplenum + 1
        cv2.imwrite("dataset/user." + str(Id) + "." + str(samplenum) + ".jpg", +grey[y:y + h, x:x + w])
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.waitKey(100)
    cv2.imshow("Face",img)
    cv2.waitKey(1)
    if samplenum > 20:
        break
cam.release()
cv2.destroyAllWindows()
