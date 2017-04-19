from tkinter import *
if __name__ == '__main__':
    root = Tk()
    for fm in ['red', 'blue', 'yellow', 'green', 'white', 'black']:
        Frame(hight=20, width=400, bg=fm).pack()
    root.mainloop()
