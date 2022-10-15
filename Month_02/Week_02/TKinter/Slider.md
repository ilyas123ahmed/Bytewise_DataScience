```python
from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.title('Learn To Code at datacamp.com')
root.iconbitmap('D:\Python\GUI_Data_Science\icon.ico')
root.geometry("800x800")

vertical = Scale(root, from_=0, to=400)
vertical.pack()

def slide():
	my_label = Label(root, text=horizontal.get()).pack()
	root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))

horizontal = Scale(root, from_=0, to=600, orient=HORIZONTAL)
horizontal.pack()

my_label = Label(root, text=horizontal.get()).pack()



my_btn = Button(root, text="Click Me!", command=slide).pack()

root.mainloop()
```

### OUTPUT TERMIANL
