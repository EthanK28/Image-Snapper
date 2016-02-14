import requests


changed_name = ''
image_address = ''

f = open(changed_name, 'wb')
f.write(requests.get(image_address).content)
f.close()