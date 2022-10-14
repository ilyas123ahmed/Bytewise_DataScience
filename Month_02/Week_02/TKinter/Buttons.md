```python
from tkinter import *

root = Tk()

def myClick():
	myLabel = Label(root, text="Look! I clicked a Button!!")
	myLabel.pack()

myButton = Button(root, text="Click Me!", command=myClick,padx=30,pady=30)
#myButton = Button(root, text="Click Me!", command=myClick,padx=30,pady=30,fg='green',bg='pink')
myButton.pack()



root.mainloop()
```

### OUTPUT TERMINAL
![image](https://user-images.githubusercontent.com/80588277/195858317-be9fa51a-4b30-4c6e-a111-7ea3076b7c1a.png)

![image](https://user-images.githubusercontent.com/80588277/195859155-40be1063-1377-44c0-95f7-cd4cccc64869.png)

