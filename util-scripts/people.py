import requests
from io import StringIO
from PIL import Image
from io import BytesIO
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

DEPT_TREE_URL = 'https://isearch.asu.edu/endpoints/dept_tree/json'
DEPT_PROFILE_URL = 'https://isearch.asu.edu/endpoints/dept-profiles/json/'
DEPT_NID_KEY = 'dept_nid'
ASURITE_ID_KEY = 'asuriteId'
PHOTO_URL_KEY = 'photoUrl'
STORE_LOCATION = '/home/hkayaroh/util-scripts/fol1/'

response = requests.get(DEPT_TREE_URL)
data = response.json()
from nested_lookup import nested_lookup

# https://github.com/russellballestrini/nested-lookup/
dept_ids = nested_lookup(DEPT_NID_KEY, data)

asuriteid_and_imageurls = []

for dept_id in dept_ids:
    try:
        response = requests.get(DEPT_PROFILE_URL + str(dept_id))
        profiles = response.json()
        for profile in profiles:
            asuriteid_and_imageurls.append({
                'asurite_id' : profile[ASURITE_ID_KEY],
                'image_url' : profile[PHOTO_URL_KEY]
            })
    except ValueError:
        print('JSON decod failed. May be...')
    except:
        profile('generic error')

print('number of people ' + str(len(asuriteid_and_imageurls)))
for item in asuriteid_and_imageurls:
    try:
        r = requests.get(item['image_url'])
        if r.status_code == 200:
            i = Image.open(BytesIO(r.content))
            i.save(STORE_LOCATION + item['asurite_id'] + '.png')
    except:
        print('error while parsing image')
