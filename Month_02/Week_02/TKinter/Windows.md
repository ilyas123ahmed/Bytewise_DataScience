```python
from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.title('Learn To Code at Codemy.com')
root.iconbitmap('D:\Python\GUI_Data_Science\icon.ico')

def open():
	global my_img
	top = Toplevel()
	top.title('My Second Window')
	top.iconbitmap('D:\Python\GUI_Data_Science\icon.ico')
	my_img = ImageTk.PhotoImage(Image.open("1.jpg"))
	my_label = Label(top, image=my_img).pack()
	btn2 = Button(top, text="close window", command=top.destroy).pack()



btn = Button(root, text="Open Second Windo", command=open).pack()

mainloop()
```

### OUTPUT TERMIANL
![image](https://user-images.githubusercontent.com/80588277/195969678-38082042-1106-4f80-95f4-97970c202371.png)
![image](https://user-images.githubusercontent.com/80588277/195969690-019a8480-8cdd-4818-bc62-6886b1f0e4f7.png)
