import cv2
import numpy as np
import sqlite3
import os

conn = sqlite3.connect('database.db')
c = conn.cursor()

fname = "recognizer/trainingData.yml"
if not os.path.isfile(fname):
    print("Please train the data first")
    exit(0)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# cap = cv2.VideoCapture(0)
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read(fname)

imageDir = "D:\Computer department\Missing people\photos"  # specify your path here
image_path_list = []
valid_image_extensions = [".jpg", ".jpeg", ".png", ".gif"]  # specify your vald extensions here
valid_image_extensions = [item.lower() for item in valid_image_extensions]

# create a list all files in directory and
# append files with a vaild extention to image_path_list
for file in os.listdir(imageDir):
    extension = os.path.splitext(file)[1]
    if extension.lower() not in valid_image_extensions:
        continue
    image_path_list.append(os.path.join(imageDir, file))

# loop through image_path_list to open each image
for imagePath in image_path_list:
    img = cv2.imread(imagePath)

    # display the image on screen with imshow()
    # after checking that it loaded
    if img is not None:
        cv2.imshow(imagePath, img)
    elif img is None:
        print("Error loading: " + imagePath)
        # end this loop iteration and move on to next image
        continue
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
        ids, conf = recognizer.predict(gray[y:y+h, x:x+w])
        c.execute("select name from users where id = (?);", (ids,))
        result = c.fetchall()
        name = result[0][0]
        if conf < 50:
            cv2.putText(img, name, (x+2, y+h-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (150, 255, 0), 2)
        else:
            cv2.putText(img, 'No Match', (x+2, y+h-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow('Face Recognizer', img)
    k = cv2.waitKey(0) & 0xff
    if k == 27:
        break

# cap.release()
# cv2.destroyAllWindows()
