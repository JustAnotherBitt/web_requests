# simpler than urllib

import requests

headers = {"User-Agent": "",
             "Cookie": ""}

data = {"user": "", "password": ""}

response = requests.post("http://", headers=headers, data=data)
html = response.text
print(html)