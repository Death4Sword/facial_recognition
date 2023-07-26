import cv2
from simple_facerec import SimpleFacerec
from text_to_audio import text_to_audio_func
import threading
import os

# Encode faces from a folder
sfr = SimpleFacerec()
# sfr.load_encoding_images("images")
sfr.load_encoding_images("dataset/antoine")
sfr.load_encoding_images("dataset/messi")

# Load Camera
cap = cv2.VideoCapture("/dev/video2")
# cap = cv2.VideoCapture(0)
cap.set(3,640) # set Witdh
cap.set(4,480) # set Height

imgBackground = cv2.imread('ressources/background.png')

face_names = "Unknown"

while True:
    ret, frame = cap.read()
    # Detect Faces
    
    before_faces = face_names
    face_locations, face_names = sfr.detect_known_faces(frame)
    for face_loc, name in zip(face_locations, face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

        cv2.putText(frame, str(name[0]),(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2) # str(name[value_get_person_to_print])
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)
    # if detected -> if always same name --> one print only with no actualisation
    imgBackground[355:355+480,97:97+640] = frame
    #cv2.imshow("Frame", frame)
    cv2.imshow('Face attendance', imgBackground)

    key = cv2.waitKey(1)
    if key == 27:
        break
    if before_faces != face_names :
        if not face_names:
            print("You are not in the database !")
            pass
        elif face_names[0] == before_faces:
            print("I already know you !")
        elif face_names[0] != "Unknown":            
            t1 = threading.Thread(target=text_to_audio_func, args=face_names)
            t1.start()
            
cap.release()
cv2.destroyAllWindows()