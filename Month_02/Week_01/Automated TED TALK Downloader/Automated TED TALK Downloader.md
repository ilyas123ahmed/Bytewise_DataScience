# Custom TED TALK Video Downloader
```python
# Custom Code to download TED TALK Video
# getting content of the TED Talk page
import requests
# web scraping
from bs4 import BeautifulSoup
# Regular Expression pattern matching
import re
# for argument parsing
import sys
# to save extract data in json format
import json
# from urllib.request import urlretrieve #downloading mp4

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

file_name = user_name+'automated_Video.mp4'
with open(file_name,'wb') as f:
    f.write(mp4_response.content)
```

### Terminal View

![image](https://user-images.githubusercontent.com/80588277/193449083-170591b9-7df3-48e5-8387-f77883163351.png)

### Project View
![image](https://user-images.githubusercontent.com/80588277/193449064-c30fc948-3f9e-42cf-8733-ba9e01146c55.png)



# Automated TED TALK Video Downloader
```python
# Automated TED TALK Downlod Video
#getting content of the TED Talk page
import requests
#web scraping
from bs4 import BeautifulSoup
#Regular Expression pattern matching
import re
#for argument parsing
import sys
# from urllib.request import urlretrieve #downloading mp4


# Exception Handling
if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    sys.exit("Error: Please enter the TED Talk URL")


url = input("Please Enter Your Ted Talk URL : ")
r = requests.get(url)

print("Download about to start")

soup = BeautifulSoup(r.content, features="lxml")
result=''
for val in soup.findAll("script"):
    if(re.search("resources",str(val))) is not None:
        result = str(val)

result_mp4 = re.search("(?P<url>https?://[^\s]+)(mp4)", result).group("url")
result_mp4=result_mp4+'mp4'
mp4_url = result_mp4.split('"')[0]

print("Downloading video from : " + result_mp4)
file_name = mp4_url.split("/")[len(mp4_url.split("/"))-1].split('?')[0]

print("Storing video in : " + file_name)


r = requests.get(mp4_url)

user_name = input("Please Enter The File Name : ")
file_name = user_name+'automated_Video.mp4'
with open(file_name,'wb') as f:
    f.write(r.content)

print("Download Process finished")

```

### Terminal View
![image](https://user-images.githubusercontent.com/80588277/193448554-f97735d7-1e00-4779-85a0-913ccd5624e5.png)


### Project View
![image](https://user-images.githubusercontent.com/80588277/193448584-6609426d-cdb9-4fb5-b2d6-b193ea1f3eb6.png)
