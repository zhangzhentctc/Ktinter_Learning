from tkinter import *
root = Tk()
for i in range(1, 101):
    val = str(i)
Label(root, textvariable = val).pack()
root.mainloop()