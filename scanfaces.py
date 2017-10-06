import cv2
import os
import argparse
import base64
import numpy as np
print(np.__version__)
print('**************************')


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
    print(response.json())
    print(type(response.json()))

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

def get_info(img_base64, outputdir):
    image_name = '/home/hkayaroh/attendance/groupimg/IMG_0092.jpg'
    with open(image_name, 'rb') as img:
        img_binary = img.read()
        import base64
        img_base64 = base64.b64encode(img_binary)
    faces = get_faces(img_base64)
    num_faces = 0
    import sys
    print(sys.version_info)
    print(np.__version__)
    print('**************************')

    for face in faces:
        face_filename = os.path.join(outputdir, "face{}.png".format(num_faces))
        cv2.imwrite(face_filename, face)
        num_faces += 1

        #img = face.tobytes()
        #print(img)
        #face = base64.b64encode(img)
        #get_face_info(face)
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Extract faces from photos.')
    parser.add_argument('outputdir', type=str, help='Output directory for faces')
    args = parser.parse_args()
    get_info("binary", args.outputdir)    

