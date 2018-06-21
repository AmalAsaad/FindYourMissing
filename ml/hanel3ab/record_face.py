import cv2
import numpy as np
import sqlite3
import os

d = 0
conn = sqlite3.connect('database.db')
if not os.path.exists('./dataset'):
    os.makedirs('./dataset')

c = conn.cursor()

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# cap = cv2.VideoCapture(0)

uname = input("Enter your name: ")

c.execute('INSERT INTO users (name) VALUES (?)', (uname,))

uid = c.lastrowid

sampleNum = 0

# while True:
#     ret, img = cap.read()

os.chdir('/Computer department/Missing people/pyhton programs for project/haarcascade')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# image path and valid extensions
imageDir = r"D:\Computer department\Missing people\test"  # specify your path here
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
    cv2.imwrite(
        "D:\Computer department\Missing people\pyhton programs for project\detected\scaled_%d.jpeg" % d, gray)
    d += 1
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        sampleNum = sampleNum+1
        cv2.imwrite("dataset/User."+str(uid)+"."+str(sampleNum)+".jpg", gray[y:y+h, x:x+w])
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.waitKey(100)
    cv2.imshow('img', img)
    cv2.waitKey(1)
    if sampleNum > 20:
        break
# cap.release()

conn.commit()

conn.close()
cv2.destroyAllWindows()
