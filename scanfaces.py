import cv2
import os
import argparse
import base64
from PIL import Image
from StringIO import StringIO
import numpy as np

def readb64(base64_string):
    nparr = np.fromstring(base64_string.decode('base64'), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return img

def get_faces(base64_string):
    face_cascade = cv2.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_eye.xml')
    img = readb64(base64_string)
    print(img)
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


def scan_images(root_dir, output_dir):
    image_extensions = ["jpg", "png"]
    num_faces = 0
    num_images = 0

    print("Images directory {}".format(root_dir))
    print("Output directory {}".format(output_dir))
    print("-" * 20)

    for dir_name, subdir_list, file_list in os.walk(root_dir):
        print('Scanning directory: %s' % dir_name)
        for filename in file_list:
            extension = os.path.splitext(filename)[1][1:]
            if extension in image_extensions:
                faces = get_faces(os.path.join(dir_name, filename))
                num_images += 1

                for face in faces:
                    face_filename = os.path.join(output_dir, "face{}.png".format(num_faces))
                
                    print(type(face))
                    print(face)
                    cv2.imwrite(face_filename, face)
                    print("\tWrote {} extracted from {}".format(face_filename, filename))
                    num_faces += 1

    print("-" * 20)
    print("Total number of images: {}".format(num_images))
    print("Total number of faces: {}".format(num_faces))

def get_info(img_base64, outputdir):
    image_name = '/home/hkayaroh/attendance/groupimg/IMG_0092.jpg'
    with open(image_name, 'rb') as img:
        img_binary = img.read()
        import base64
        img_base64 = base64.b64encode(img_binary)
    faces = get_faces(img_base64)
    num_faces = 0
    for face in faces:
        face_filename = os.path.join(outputdir, "face{}.png".format(num_faces))
        cv2.imwrite(face_filename, face)
        num_faces += 1
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Extract faces from photos.')
    parser.add_argument('outputdir', type=str, help='Output directory for faces')
    args = parser.parse_args()
    get_info("binary", args.outputdir)    

