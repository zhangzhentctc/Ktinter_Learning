from tkinter import *
if __name__ == '__main__':
    root = Tk()
    fm =[]
    for color in ['red', 'blue']:
        fm.append(Frame(height=200, width=400, bg=color))
    Label(fm[1], text='Hello Lable').pack()
    fm[0].pack()
    fm[1].pack()
    root.mainloop()
