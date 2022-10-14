```python
from tkinter import *

root = Tk()

def myClick():
	myLabel = Label(root, text="Look! I clicked a Button!!")
	myLabel.pack()

myButton = Button(root, text="Click Me!", command=myClick,padx=30,pady=30)
myButton.pack()



root.mainloop()
```

### OUTPUT TERMINAL
