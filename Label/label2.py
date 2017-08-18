from tkinter import *
import time
if __name__ == '__main__':
    green_file = './green.gif'
    red_file = './red.gif'
    root = Tk()
    #label1 = Label(root, bitmap='error')
    #label1.pack()


    bm_green = PhotoImage(file=green_file)
    label_green = Label(root, image=bm_green)
    label_green.pack()

    bm_red = PhotoImage(file=red_file)
    label_red = Label(root, image=bm_red)
    label_red.pack()

    #bm_green = PhotoImage(file=green_file)
    #label_green = Label(root, image=bm_green)
    #label_green.pack()


    root.update_idletasks()
    #while(1):
        #i=1
    root.mainloop()



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