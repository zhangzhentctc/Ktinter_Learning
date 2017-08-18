from tkinter import *
import time
import math
import random

X_COUNT = 3
Y_COUNT = 3

ERROR = -1
RET_OK = 0
class smile_game():
    def __init__(self):
        self.width_new = 150
        self.height_new = 150
        self.right_x = 0
        self.right_y = 0
        self.positive_faces = 1
        self.negative_faces = 1

    def show_new(self):
        self.right_x = random.randint(0, X_COUNT - 1)
        self.right_y = random.randint(0, Y_COUNT - 1)

        for x in range(0, X_COUNT):
            for y in range(0, Y_COUNT):
                if x == self.right_x and y == self.right_y:
                    ret, image = self.get_positive_face()
                    if ret == ERROR:
                        return ERROR
                else:
                    ret, image = self.get_negative_face()
                    if ret == ERROR:
                        return ERROR
                self.cv.create_image(((x * 2 + 1) * self.width_new / 2, (y * 2 + 1) * self.height_new / 2), image=image)
        return RET_OK


    def button_callback(self,event):
        print ("clicked at", event.x, event.y)
        self.x_num = math.floor(event.x / self.width_new)
        self.y_num = math.floor(event.y / self.height_new)
        self.cv.delete("all")
        time.sleep(0.3)
        self.show_new()


    def motion_callback(self,event):
        self.x_num = math.floor(event.x / self.width_new)
        self.y_num = math.floor(event.y / self.height_new)
        #print("right", self.right_x, self.right_y)
        #print("now", self.x_num, self.y_num)

        if self.x_num == self.right_x and self.y_num == self.right_y:
            self.draw_outline(self.x_num, self.y_num, "green")
        else:
            self.draw_outline(self.x_num, self.y_num, "red")


    def draw_outline(self, num_x, num_y, color):
        self.cv.delete("rectangle")
        if num_x > X_COUNT - 1 or num_y > Y_COUNT - 1:
            return
        tangle = self.cv.create_rectangle(num_x * self.width_new + 1, num_y * self.height_new + 1, \
                                          (num_x + 1) * self.width_new, (num_y + 1) * self.height_new, \
                                 outline=color, tags=("rectangle"))


    def get_positive_face(self):
        positive_count = len(self.imgs_positive)
        if positive_count == 0:
            return ERROR, ""
        positive_num = random.randint(0, positive_count - 1)
        return RET_OK, self.imgs_positive[positive_num]


    def get_negative_face(self):
        negative_count = len(self.imgs_negative)
        if negative_count == 0:
            return ERROR, ""
        negative_num = random.randint(0, negative_count - 1)
        return RET_OK, self.imgs_negative[negative_num]


    def init_faces(self):
        # imgs = [PhotoImage(file='/tmp/' + str(i) + '.gif') for  i  in  range(3)]
        # self.imgs_positive = [PhotoImage(file='../Label/' + str(i) + '.gif') for i range(0,1)]
        self.imgs_positive=[]
        self.imgs_negative=[]
        for i in range(0, self.positive_faces):
            self.imgs_positive.append( PhotoImage(file='./' + 'positive_' + str(i) + '.gif'))

        for i in range(0, self.negative_faces):
            self.imgs_negative.append(PhotoImage(file='./' + 'negative_' + str(i) + '.gif'))

        #self.imgs_positive = [PhotoImage(file='../Label/green.gif')]
        #self.imgs_negative = [PhotoImage(file='../Label/red.gif')]


    def game(self):
        self.root = Tk()
        self.cv = Canvas(self.root, bg='white', width=self.width_new * X_COUNT, height=self.height_new * Y_COUNT)
        self.init_faces()

        self.show_new()
        self.cv.bind("<Button-1>", self.button_callback)
        self.cv.bind("<Motion>", self.motion_callback)
        self.cv.pack()
        self.root.mainloop()


if __name__=="__main__":
    game = smile_game()
    game.game()
