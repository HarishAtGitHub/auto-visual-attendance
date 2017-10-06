import cv2
import os
import argparse
import base64
import numpy as np

def get_face_info(img_base64):
    image_match_url = 'https://h2h2c0e7p9.execute-api.us-west-2.amazonaws.com/beta/imageinfo'
    headers = {'Content-Type' : 'application/json',
               'x-api-key' : 'h4ANNxg5AA5PpYMxu3QZg7t8C9St6KKI9rZPmrQT'}
    request_payload = {
        'image':'',
    }
    request_payload['image'] = img_base64.decode('utf-8')
    import requests
    import json
    response = requests.post(image_match_url,
                             data=json.dumps(request_payload),
                             headers=headers)
    return response.json()

def readb64(base64_string):
    nparr = np.fromstring(base64.b64decode(base64_string), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return img

def get_faces(base64_string):
    face_cascade = cv2.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_eye.xml')
    img = readb64(base64_string)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 5)

    face_images = []

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]

        eyes = eye_cascade.detectMultiScale(roi_gray)
        if len(eyes) >= 1:
            face_images.append(roi_color)

    return face_images

def get_info(img_base64):
    image_name = '/home/hkayaroh/attendance/groupimg/IMG_0092.jpg'
    with open(image_name, 'rb') as img:
        img_binary = img.read()
        import base64
        img_base64 = base64.b64encode(img_binary)
    faces = get_faces(img_base64)
    num_faces = 0
    import os
    info = []
    # FIXME : To do without saving the file. Directly numpy array to binary    
    for face in faces:
        face_filename = os.path.dirname( __file__ ) + '/res/' + "face{}.png".format(num_faces)
        cv2.imwrite(face_filename, face)
        img = face.tobytes()
        with open(face_filename, 'rb') as img_file:
            binary = img_file.read() 
        img = base64.b64encode(binary)
        info.append(get_face_info(img))
        num_faces += 1
    return info
