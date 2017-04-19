from tkinter import *
import time
if __name__ == '__main__':
    green_file = 'D:\\quant\\ktinter\\Ktinter_Learning\\Label\\green.gif'
    red_file = 'D:\\quant\\ktinter\\Ktinter_Learning\\Label\\red.gif'
    root = Tk()
    label1 = Label(root, bitmap='error')
    label1.pack()
    file = green_file
    bm = PhotoImage(file=file)
    label2 = Label(root, image=bm)
    label2.pack()
    root.update_idletasks()
    while(1):
        i=1
#    root.mainloop()
    while(0):
        file = red_file
        bm = PhotoImage(file=file)
        label2 = Label(root, image=bm)
        root.update_idletasks()
        time.sleep(1)
        file = green_file
        bm = PhotoImage(file=file)
        label2 = Label(root, image=bm)
        root.update_idletasks()
        time.sleep(1)