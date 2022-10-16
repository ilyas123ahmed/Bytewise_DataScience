```python
from tkinter import *
from PIL import ImageTk,Image
import numpy as np
import matplotlib.pyplot as plt


root = Tk()
root.title('Learn To Code at Bytewise')
root.iconbitmap('D:\Python\GUI_Data_Science\icon.ico')
root.geometry("400x400")

def graph():
	house_prices = np.random.normal(2000, 25000, 50)
	plt.hist(house_prices)
	plt.show()

my_button = Button(root, text="Create a Graph", command=graph)
my_button.pack()

root.mainloop()
```

### OUTPUT TERMINAL
![image](https://user-images.githubusercontent.com/80588277/196034125-2f720a51-a4cc-492c-8b9b-a424c060f9f9.png)
![image](https://user-images.githubusercontent.com/80588277/196034136-0b09b1c5-1ce8-41a8-95b0-319c2375cd85.png)
