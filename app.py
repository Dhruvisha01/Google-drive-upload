import json
import requests
headers = {"Authorization": "Bearer ### Your Key ###"}
para = {
    "name": "samplefile.png",
}
files = {
    'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
    'file': open("./dog.JPG", "rb")
}
r = requests.post(
    "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
    headers=headers,
    files=files
)
print(r.text)