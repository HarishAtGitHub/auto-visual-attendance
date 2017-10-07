import requests
import base64
import json

#file_name = '/home/hkayaroh/attendance/groupimg/IMG_0092.jpg'
file_name = '/home/hkayaroh/attendance/groupimg/group1.png'
#url = 'http://ec2-35-167-16-218.us-west-2.compute.amazonaws.com/vizattendance/recognize'
url = 'http://ec2-35-167-16-218.us-west-2.compute.amazonaws.com/vizattendance/recognize'


with open(file_name, 'rb') as img:
    img_binary = img.read()
    img_base64 = base64.b64encode(img_binary)
    request_payload = {'image' : img_base64.decode('utf-8')} 
    headers = {'Content-Type' : 'application/json'}
    response = requests.post(url, data=json.dumps(request_payload), headers=headers)
    print(response.json())
