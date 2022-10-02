# Image Conversion
```python
# Importing Libraries
# Python Image Library - Image Processing
from PIL import Image
import glob

# PNG to JPG
print(glob.glob("*.png"))

for file in glob.glob("*.png"):
    image = Image.open(file)
    rgb_im = image.convert('RGB')
    rgb_im.save(file.replace("png", "jpg"), quality=100)
print(glob.glob("*.jpg"))


# JPG to PNG
for file in glob.glob("*.jpg"):
    image = Image.open(file)
    rgb_im = image.convert('RGBA')
    rgb_im.save("new_"+file.replace("jpg", "png"), quality=99)
print(glob.glob("*.png"))

```

### Terminal and Project View
![image](https://user-images.githubusercontent.com/80588277/193466666-f53de3e8-22fe-4dab-a309-76eed938f449.png)

![image](https://user-images.githubusercontent.com/80588277/193466701-ddac74ef-cd32-476a-a14f-892131b097c1.png)

![image](https://user-images.githubusercontent.com/80588277/193466706-53936005-dbfc-4c2b-bb0f-0dff54808b2c.png)


### Terminal and Project View

![image](https://user-images.githubusercontent.com/80588277/193466731-2bc6ddc7-67d0-4157-98cb-27abaad40709.png)
![image](https://user-images.githubusercontent.com/80588277/193466741-e204e810-d1d1-4d93-b496-5a18ac05b883.png)
