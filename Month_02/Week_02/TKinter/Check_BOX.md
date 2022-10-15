```python
from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.title('Learn To Code at datacamp.com')
root.iconbitmap('D:\Python\GUI_Data_Science\icon.ico')
root.geometry("800x800")

def show():
	myLabel = Label(root, text=var.get()).pack()


var = StringVar()

c =Checkbutton(root, text="Would you like to SuperSize your order? Check Here!", variable=var, onvalue="SuperSize", offvalue="RegularSize")
c.deselect()
c.pack()



myButton = Button(root, text="Show Selection", command=show).pack()


root.mainloop()
```

### OUTPUT TERMINAL
![image](https://user-images.githubusercontent.com/80588277/195994800-20c735e2-67b6-466c-b337-0d7a51b146e7.png)
