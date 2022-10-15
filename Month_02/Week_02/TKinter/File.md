```python
from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

root = Tk()
root.title('Codemy.com Image Viewer')
root.iconbitmap('D:\Python\GUI_Data_Science\icon.ico')


def open():
	global my_image
	root.filename = filedialog.askopenfilename(initialdir="D:\Python\GUI_Data_Science", title="Select A File", filetypes=(("jpg files", "*.jpg"),("all files", "*.*")))
	my_label = Label(root, text=root.filename).pack()
	my_image = ImageTk.PhotoImage(Image.open(root.filename))
	my_image_label = Label(image=my_image).pack()


my_btn = Button(root, text="Open File", command=open).pack()


root.mainloop()
```

### OUTPUT TERMINAL
![image](https://user-images.githubusercontent.com/80588277/195989336-269c9b66-3182-4d52-90e5-34ba3fb53975.png)
![image](https://user-images.githubusercontent.com/80588277/195989362-bf812f15-7b3a-42e5-94ff-f248188f8eee.png)
![image](https://user-images.githubusercontent.com/80588277/195989390-d703314d-d928-4e5f-86f8-d1fbdd675937.png)
