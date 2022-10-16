```pyhton
from tkinter import *
from PIL import ImageTk, Image
import requests
import json

root = Tk()
root.title('Learn To Code at Bytewise')
root.iconbitmap('D:\Python\GUI_Data_Science\icon.ico')
root.geometry("600x200")


# Create Zipcode Lookup Function
def zipLookup():
    try:
        api_request = requests.get(
            "http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip.get() + "&distance=5&API_KEY=96A38DFD-5C56-4740-AD99-E38C0C855A1B")
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']

        if category == "Good":
            weather_color = "#0C0"
        elif category == "Moderate":
            weather_color = "#FFFF00"
        elif category == "Unhealthy for Sensitive Groups":
            weather_color = "#ff9900"
        elif category == "Unhealthy":
            weather_color = "#FF0000"
        elif category == "Very Unhealthy":
            weather_color = "#990066"
        elif category == "Hazardous":
            weather_color = "#660000"

        root.configure(background=weather_color)

        myLabel = Label(root, text=city + " Air Quality " + str(quality) + " " + category, font=("Helvetica", 20),
                        background=weather_color)
        myLabel.grid(row=1, column=0, columnspan=2)
    except Exception as e:
        api = "Error..."


zip = Entry(root)
zip.grid(row=0, column=0, sticky=W + E + N + S)

zipButton = Button(root, text="Lookup Zipcode", command=zipLookup)
zipButton.grid(row=0, column=1, sticky=W + E + N + S)

root.mainloop()
```

### OUTPUT TERMINAL
![image](https://user-images.githubusercontent.com/80588277/196033703-2940134d-efde-4db7-b925-ac6032eaecfb.png)
