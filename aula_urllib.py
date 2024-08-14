from urllib import request, parse

headers = {"User-Agent": "",
             "Cookie": ""}

data = {"user": "", "password": ""}
data = parse.urlencode(data).encode()

req = request.Request("http://", headers=headers, data=data)
response = request.urlopen(req)
html = response.read()
print(html)
