# Custom TED TALK Video Downloader 

```python
import requests
from bs4 import BeautifulSoup
import re
import sys
import json
# Automated Custom Code
url = input("Please Enter Your Ted Talk URL : ")
r = requests.get(url)
print("Download about to start")

soup = BeautifulSoup(r.content, "html.parser")
next_data_script = soup.find(id="__NEXT_DATA__")

data_json = next_data_script.string
player_data = json.loads(data_json)['props']['pageProps']['videoData']['playerData']
url_content = json.loads(player_data)['resources']['h264'][0]['file']
print(url_content)
mp4_response = requests.get(url_content)

user_name = input("Please Enter The File Name : ")

file_name = user_name+'.mp4'
with open(file_name,'wb') as f:
    f.write(mp4_response.content)
```
