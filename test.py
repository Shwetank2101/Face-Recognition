import face_recognition
import cv2
import numpy as np
import pandas as pd
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import urllib
import urllib.request


def make(request):
        config = {
            "type": "service_account",
            "project_id": "image-23704",
            "private_key_id": "3356ea3be1eacd942f2e46b16924c2fc1d821dd1",
            "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDI1Nxc9eHSPeYB\nSNfMWzkKuEQU6YknVm6OtT8zghD84sZ3GHFmGs2QsHRjTdxj6fSwRoYnPnemUB/M\npDjDotKNjbni4KFkqB69gQhTWxJeREZtjsLfWhtxCaSEH0bbzMWFpEkxl5ds8FiR\npq9f5p4gGs1cMTlURlsEzixE/Ue1tnf9+pBKerqy7OzAWXLgbPaqHv6BMPqBwKHS\nwqftXlBy6idxRM+4BV5gzHD9ASdms1rvsOzOfog6SURmbgEtuURzr6s5AUOwutut\npmPu3sjeR6aPLzB4e6H30MzIYT60cxQuFAYyBSJ+8dRQUoqsS6qKwXULwl85epvY\nmC8DK0jlAgMBAAECggEABYYWnwQSkxjlWMyyrKn0dg8vvcukD5iPOl9rGm6c1Zp4\npoKqxBJ7QUsKxc+FmJtkTqDDjRz6CXFiqsoaeXSnH07+7JSdtFTQYcUaBFrHzoWe\nJ8BnXp0dBcbfnqE47pzOaESASBN6J6bhW2y+82G/OkH2uwiWXaZnNZ5TkZZWfp+2\nePD5vbBqi56JuTkZeuu82TVlmMsRoKnnNP6YmZ0nfv6Q9yTHKT3c1WbZCJvOg8sP\nRuo7ZPsAqPWcBKO2F6N9VGij7xWV84gqaAD/k9s/337kvr1c9+cfWmkI7TY19g3h\n7b2ltbBBQ/PAS2ZcHfAsNhC3ub5l34fbJRaaJOeo8wKBgQD9R5ZksYOFHo8GMt6K\n6RWYoyY412cZo82JvCBg8lF/cuQYaK+2IU5yB3+7LdopB477XpAkijoTopecnpJx\ngUWImdqCnIZv1yt/bDWzVWLs6y2VLSgbJJgt9XLAiJGdtBo/55996JrjTbQdUlwB\nvjXorJhW7rbifjD8ESucV3jerwKBgQDK/RAdt74gbYM3oLYGE4GIVno46eRFrDW9\nF4wPuV9Xt8KJ7mW1EbIM/XGmM+LK3agoWm4k0bNVfau7S/XQ7x+Z4BOISVMPyzpR\newwm6IwOAVFpdD9kmmqyAD0gjmKfh4F0OVYDvoF+F4TZwFBjbELyGNgC77V2p2CE\nNh8uiUyWqwKBgAwxbREN5qn67aG7wzDmxa5idE2aORFn7FYsI1bnc3ryOf7e006u\nTct5hvGo5G7DOWPqin/n06HsWuYkUCJ8ua840Ocmx+YMcsCgofkvLCMBs2ESGnMs\nENNtlIemS3RPHlBjQy9ZilNVA03CEEHZOVkpLfBJb655qrwHy5SsNVprAoGBALRn\n8VjYIuwjKInaFayUzXzkjr/ib/TUNvaV5O9cqzYEpat863vf/ES7Q7SZTKlMEtW6\neUXT8fS7OlO+EPzeaVGS6wknUeEpl+0u1QAHkeIonbiBjo3VB5qnx6wVn+V0w0MO\najntqJzuPi5hU5DpeR49ok4JyVdpLsiSaWgsspr9AoGAIsFvGL3HCv73UbUyybWX\n9DLEc8M2bNgOFvOWWRj7NsKTm2zagutz/6DcVgXhI/Uct9xn1FDTblAX5IOwMkXz\noFveCJBeVpQcu11J0M7naEg6buv0mpX7DscAZMT1nP9rnEXwyFDuX3wYPvK0PMHH\nRUotg0rctiv9ps4Mw7/NR4w=\n-----END PRIVATE KEY-----\n",
            "client_email": "firebase-adminsdk-a3tb3@image-23704.iam.gserviceaccount.com",
            "client_id": "116186165584908361579",
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-a3tb3%40image-23704"
                                    ".iam.gserviceaccount.com "
        }
        cred = credentials.Certificate(config)
        firebase_admin.initialize_app(cred)
        db = firestore.client()
        user = db.collection('image').document('images').get().to_dict()
        Name = list(user.keys())
        Urls = list(user.values())
        images = []
        classNames = []
        req = urllib.request.urlopen(Urls[0])
        arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
        img = cv2.imdecode(arr, -1)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        print('Attendence')
        video_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)

        # Load a sample picture and learn how to recognize it.
        # obama_image = face_recognition.load_image_file("static/Pictures/obama.jpg")
        # print(obama_image)
        obama_face_encoding = face_recognition.face_encodings(img)[0]

        # # Load a second sample picture and learn how to recognize it.
        # biden_image = face_recognition.load_image_file("static/Pictures/biden.jpg")
        # biden_face_encoding = face_recognition.face_encodings(biden_image)[0]

        # shwetank_image = face_recognition.load_image_file("static/Pictures/Shwetank.jpg")
        # shwetank_face_encoding = face_recognition.face_encodings(shwetank_image)[0]

        # dixant_image = face_recognition.load_image_file("static/Pictures/Dixant.jpg")
        # dixant_face_encoding = face_recognition.face_encodings(dixant_image)[0]

        # shivi_image = face_recognition.load_image_file("static/Pictures/shiviiii.jpg")
        # shivi_face_encoding = face_recognition.face_encodings(shivi_image)[0]

        # shobhit_image = face_recognition.load_image_file("static/Pictures/Shobhit.jpg")
        # shobhit_face_encoding = face_recognition.face_encodings(shobhit_image)[0]

        # praveen_image = face_recognition.load_image_file("static/Pictures/Praveen.jpg")
        # praveen_face_encoding = face_recognition.face_encodings(praveen_image)[0]

        # anju_image = face_recognition.load_image_file("static/Pictures/anju.jpg")
        # anju_face_encoding = face_recognition.face_encodings(anju_image)[0]
        # Create arrays of known face encodings and their names
        known_face_encodings = [
            obama_face_encoding,
            # biden_face_encoding,
            # shwetank_face_encoding,
            # dixant_face_encoding,
            # shivi_face_encoding,
            # shobhit_face_encoding,
            # praveen_face_encoding,
            # anju_face_encoding
            
            
        ]
        known_face_names = [
            "Barack Obama",
            # "Joe Biden",
            # "Shwetank Dixit",
            # "Dixant Dixit",
            # "Shiviii",
            # "Shobhit Mishraji",
            # "Praveen Tyagi",
            # "Anju Tyagi"
        ]

        # Initialize some variables
        face_locations = []
        face_encodings = []
        face_names = []
        process_this_frame = True
        from collections import defaultdict as dt
        my_faces=dt(lambda:1)
        list_faces=dt(list)
        my_faces["Unknown"]=0
        count=1
        while True:
            # Grab a single frame of video
            ret, frame = video_capture.read()

            # Resize frame of video to 1/4 size for faster face recognition processing
            # small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            #print(small_frame)

            # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
            rgb_small_frame = frame[:, :, ::-1]

            # Only process every other frame of video to save time
            if process_this_frame:
                # Find all the faces and face encodings in the current frame of video
                face_locations = face_recognition.face_locations(rgb_small_frame)
                face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

                face_names = []
                s=''
                for face_encoding in face_encodings:
                    # See if the face is a match for the known face(s)
                    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                    name = "Unknown"

                    # # If a match was found in known_face_encodings, just use the first one.
                    # if True in matches:
                    #     first_match_index = matches.index(True)
                    #     name = known_face_names[first_match_index]

                    # Or instead, use the known face with the smallest distance to the new face
                    face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                    best_match_index = np.argmin(face_distances)
                    if matches[best_match_index]:
                        name = known_face_names[best_match_index]
                        
                    if my_faces[name]:
                        s=s+name+' '
                        print(name)
                        list_faces[count]+=[name]
                        my_faces[name]=0
                    #print(name)
                        face_names.append(name)
                process_this_frame = not process_this_frame


            # Display the results\
            #print(1)
            for (top, right, bottom, left), name in zip(face_locations, face_names):
                # Scale back up face locations since the frame we detected in was scaled to 1/4 size
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4

                # Draw a box around the face
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

                # Draw a label with a name below the face
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

            # Display the resulting image
            cv2.imshow('Video', frame)

            # Hit 'q' on the keyboard to quit!
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release handle to the webcam
        video_capture.release()
        cv2.destroyAllWindows()
        return (request)

make(5)