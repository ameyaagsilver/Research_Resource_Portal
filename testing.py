import requests
from pathlib import Path
from pprint import pprint
url = 'https://e520-34-76-92-61.ngrok.io/file'
CurrentFolder = Path.cwd()


imageFile = CurrentFolder / 't.py'
fileData = {'file': imageFile.open(mode='rb')}
print(fileData)
r = requests.post(url, files=fileData)
# pprint(r.json())
print(r.text)