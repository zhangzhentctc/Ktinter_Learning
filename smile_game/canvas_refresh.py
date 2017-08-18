'''
Created on May 2, 2016

@author: Billal Begueradj
'''
import tkinter as Tk
from PIL import Image, ImageTk

class Begueradj(Tk.Frame):
    '''
    Dislay an image on Tkinter.Canvas and delete it on button click
    '''
    def __init__(self, parent):
        '''
        Inititialize the GUI with a button and a Canvas objects
        '''
        Tk.Frame.__init__(self, parent)
        self.parent=parent
        self.initialize_user_interface()

    def initialize_user_interface(self):
        """
        Draw the GUI
        """
        self.parent.title("Billal BEGUERADJ: Image deletion")
        self.parent.grid_rowconfigure(0,weight=1)
        self.parent.grid_columnconfigure(0,weight=1)
        self.parent.config(background="lavender")

        # Create a button and append it  a callback method to clear the image
        self.deleteb = Tk.Button(self.parent, text = 'Delete', command = self.delete_image)
        self.deleteb.grid(row = 0, column = 0)

        self.canvas = Tk.Canvas(self.parent, width = 265, height = 200)
        self.canvas.grid(row = 1, column = 0)

        # Read an image from my Desktop
        self.image = Image.open("../Label/green.gif")
        self.photo = ImageTk.PhotoImage(self.image)
        # Create the image on the Canvas
        self.canvas.create_image(132,100, image = self.photo)

    def delete_image(self):
        '''
        Callback method to delete image
        '''
        self.canvas.delete("all")


# Main method
def main():
    root=Tk.Tk()
    d=Begueradj(root)
    root.mainloop()

# Main program
if __name__=="__main__":
    main()