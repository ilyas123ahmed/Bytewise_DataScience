```python
from tkinter import *

root = Tk()

e = Entry(root, width=50, font=('Helvetica', 24))
e.pack()
e.insert(0, "Enter Your Name: ")

def myClick():
	hello = "Hello " + e.get()
	myLabel = Label(root, text=hello)
	e.delete(0, 'end')
	myLabel.pack()

myButton = Button(root, text="Enter Your Stock Quote", command=myClick)
myButton.pack()



root.mainloop()
```
### OUTPUT TERMINAL
![image](https://user-images.githubusercontent.com/80588277/195862536-76deac82-fb73-404e-bb9e-f22d6cdec90e.png)
![image](https://user-images.githubusercontent.com/80588277/195862575-495b5d6d-6bca-41a8-a933-312288807473.png)
