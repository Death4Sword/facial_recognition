# import face_recognition
# import cv2
# import os
# import glob
# import numpy as np

# class SimpleFacerec:
#     def __init__(self):
#         self.known_face_encodings = []
#         self.known_face_names = []
#         self.images_folder_names = []
#         # self.images_folder_names =""
#         # Resize frame for a faster speed
#         self.frame_resizing = 0.25
   

#     def load_encoding_images(self, images_path):
#         # """
#         # Load encoding images from path
#         # :param images_path:
#         # :return:
#         # """
#         # # Load Images
#         # self.images_folder_names = os.path.basemane(images_path)
#         # images_path = glob.glob(os.path.join(images_path, "*.*"))

#         # print("{} encoding images found.".format(len(images_path)))


#         # SHIT STORM A DELETE SI MARCHE PAS RETOUR EN ARRIERE POSSIBLE !!!!!!!!!!
#         """
#         Load encoding images from path
#         :param images_path:
#         :return:
#         """
    


#         # Get the folder name from the images_path and set it to self.images_folder_name
#         self.images_folder_names.append(os.path.basename(images_path))
#         print("Loading encoding images from folder:", self.images_folder_names)

#         # Load Images
#         images_path = glob.glob(os.path.join(images_path, "*.*"))
#         # SHIT STORM A DELETE SI MARCHE PAS RETOUR EN ARRIERE POSSIBLE !!!!!!!!!!!




#         # Store image encoding and names
#         for img_path in images_path:
#             img = cv2.imread(img_path)
#             rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#             # Get the filename only from the initial file path.
#             basename = os.path.basename(img_path)
#             (filename, ext) = os.path.splitext(basename)
#             print(os.path.basename(basename))
#             # Get encoding
#             img_encoding = face_recognition.face_encodings(rgb_img)[0]

#             # Store file name and file encoding
#             self.known_face_encodings.append(img_encoding)
#             self.known_face_names.append(filename)
#         print("Encoding images loaded")

#     def detect_known_faces(self, frame):
#         small_frame = cv2.resize(frame, (0, 0), fx=self.frame_resizing, fy=self.frame_resizing)

#         # Find all the faces and face encodings in the current frame of video
#         # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
#         rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
#         face_locations = face_recognition.face_locations(rgb_small_frame)
#         face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

#         face_names = []
#         for face_encoding in face_encodings:
#             # See if the face is a match for the known face(s)
#             matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
#             name = "Unknown"

#             # # If a match was found in known_face_encodings, just use the first one.
#             # if True in matches:
#             #     first_match_index = matches.index(True)
#                 # name = known_face_names[first_match_index]


#             # Or instead, use the known face with the smallest distance to the new face
#             face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
#             best_match_index = np.argmin(face_distances)
#             if matches[best_match_index]:
#                 name = self.images_folder_names # get the value of which folder is used. .. . . . .  . . . ; .;
#             else :
#                 name = "Unknown"
#                 # name = self.known_face_names[best_match_index] 
#             # name = self.images_folder_names if matches[best_match_index] else "Unknown"
#             face_names.append(name)
            
            
#         # Convert to numpy array to adjust coordinates with frame resizing quickly
#         face_locations = np.array(face_locations)
#         face_locations = face_locations / self.frame_resizing
#         return face_locations.astype(int), face_names

import face_recognition
import cv2
import os
import glob
import numpy as np

class Facerec:
    def __init__(self, name, index_start, index_end):
        self.name = name
        self.index_start = index_start
        self.index_end = index_end


class SimpleFacerec:
    def __init__(self):
        self.known_face_encodings = []

        self.images_folder_names = []
        # Resize frame for a faster speed
        self.frame_resizing = 0.25

        # List of FaceRec objects
        self.face_rec_list = []

    def register_faces(self, workdir): # workdir=dataset
        # gets all the folders in the dataset folder
        face_dirs = os.listdir(workdir)

        # Iterate through each person in the dataset
        for face_dir in face_dirs:
            index_start = len(self.known_face_encodings)

            images_path = os.path.join(workdir, face_dir) # images_path=dataset/antoine
            self.load_encoding_image(images_path)

            index_end = len(self.known_face_encodings)-1

            # Create a FaceRec object
            face_rec = Facerec(face_dir, index_start, index_end)
            # DEBUG print('index_start ', index_start, 'index_end ', index_end)

            # Add FaceRec object to the list
            self.face_rec_list.append(face_rec)

    def load_encoding_image(self, images_path): # images_path=dataset/antoine
        print("Loading encoding images from folder:", images_path)

        images_list_path = glob.glob(os.path.join(images_path, "*.*"))

        # Store image encoding and names
        for img_path in images_list_path:
            img = cv2.imread(img_path)
            rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            # Get the filename only from the initial file path.
            basename = os.path.basename(img_path)
            (filename, ext) = os.path.splitext(basename)
            print(os.path.basename(basename))
            # Get encoding
            img_encoding = face_recognition.face_encodings(rgb_img)[0]

            # Store file name and file encoding
            self.known_face_encodings.append(img_encoding)
        print("Encoding images loaded")

    def detect_known_faces(self, frame):
        small_frame = cv2.resize(frame, (0, 0), fx=self.frame_resizing, fy=self.frame_resizing)

        # Find all the faces and face encodings in the current frame of video
        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
            name = "Unknown"

            # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = self.detect_unknown_faces(best_match_index)
                # DEBUG print('debug best_matches_index ', best_match_index, 'debug name ', name)
            face_names.append(name)

        # Convert to numpy array to adjust coordinates with frame resizing quickly
        face_locations = np.array(face_locations)
        face_locations = face_locations / self.frame_resizing
        return face_locations.astype(int), face_names


    def detect_unknown_faces(self, best_match_index):
        for face_rec in self.face_rec_list:
            if face_rec.index_start <= best_match_index and face_rec.index_end >= best_match_index:
                return face_rec.name
        return "Unknown"