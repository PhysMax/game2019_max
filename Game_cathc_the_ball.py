from tkinter import *
from random import randrange as rnd, choice
import math

root = Tk()
root.geometry('800x600')

canv = Canvas(root, width=800, height=600, bg='white')
canv.pack(fill=BOTH, expand=1)

colors = ['red', 'orange', 'yellow', 'green', 'blue']


def move_ball():
    global x, y, move_x, move_y
    for i in range(len(ball)):
        canv.move(ball[i], move_x[i], move_y[i])
        x[i] = x[i] + move_x[i]
        y[i] = y[i] + move_y[i]
        if x[i] + r[i] >= 800:
            move_x[i] = rnd(-10, -1)
            move_y[i] = rnd(-10, 10)
        elif x[i] - r[i] <= 0:
            move_x[i] = rnd(1, 10)
            move_y[i] = rnd(-10, 10)
        if y[i] + r[i] >= 600:
            move_y[i] = rnd(-10, -1)
            move_x[i] = rnd(-10, 10)
        elif y[i] - r[i] <= 0:
            move_y[i] = rnd(1, 10)
            move_x[i] = rnd(-10, 10)
    root.after(30, move_ball)


def new_ball(l):
    """ (x,y) - center of ball, r - radius, (move_x, move_y) - vector of speed, ball - index of object """
    global x, y, r, move_x, move_y, ball
    for k in range(l):
        x.append(rnd(100, 700))
        y.append(rnd(100, 500))
        r.append(rnd(30, 50))
        move_x.append(rnd(-10, 10))
        move_y.append(rnd(-10, 10))
        ball.append(canv.create_oval(x[k] - r[k], y[k] - r[k], x[k] + r[k], y[k] + r[k], fill=choice(colors), width=0))


def move_square():
    global x_sq, y_sq, sq_move_x, sq_move_y
    for c in range(len(square)):
        canv.move(square[c], sq_move_x[c], sq_move_y[c])
        x_sq[c] = x_sq[c] + sq_move_x[c]
        y_sq[c] = y_sq[c] + sq_move_y[c]
        if x_sq[c] + side[c] >= 800:
            sq_move_x[c] = rnd(-25, -1)
        elif x_sq[c] <= 0:
            sq_move_x[c] = rnd(1, 25)
        if y_sq[c] + side[c] >= 600:
            sq_move_y[c] = rnd(-25, -1)
        elif y_sq[c] <= 0:
            sq_move_y[c] = rnd(1, 25)
    root.after(30, move_square)


def new_square(l):
    """ (x_sq, y_sq) - left-upper corner of square, side - length of side square,
     (sq_move_x, sq_move_y) - vector of speed,square - index of object """
    global x_sq, y_sq, side, sq_move_x, sq_move_y, square
    for k in range(l):
        x_sq.append(rnd(100, 700))
        y_sq.append(rnd(100, 500))
        side.append(rnd(30, 50))
        sq_move_x.append(rnd(-25, 25))
        sq_move_y.append(rnd(-25, 25))
        square.append(canv.create_rectangle(x_sq[k], y_sq[k], x_sq[k] + side[k], y_sq[k] + side[k], fill=choice(colors),
                                            width=0))


score = [0, 0]


def click(event):
    """ score[0] - number of points, score[1] - number of clicks """
    score[1] += 1
    for i in range(len(ball)):
        if math.sqrt((x[i] - event.x) ** 2 + (y[i] - event.y) ** 2) <= r[i]:
            score[0] += 1
    for i in range(len(square)):
        if (event.x >= x_sq[i]) and (event.x <= x_sq[i] + side[i]) and (event.y >= y_sq[i]) and (
                event.y <= y_sq[i] + side[i]):
            score[0] += 2
    score_line = Label(canv, text="Score: " + str(score[0]) + " out of " + str(score[1]), font="Arial 14")
    score_line.place(x=0, y=30)


user_name = input("User name: ")


def write_score():
    global user_name, score
    file = open('players.txt', 'a')
    file.write("[" + user_name + "," + str(score) + "]" + "\n")
    file.close()
    exit()


user_line = Label(canv, text="User name: " + user_name, font="Arial 14")
user_line.place(x=0, y=0)

btn = Button(canv, text="Write score", font="Arial 14", command=write_score)
btn.place(anchor=NE, x=800, y=0)

"""sets n moving balls"""
x, y, r, move_x, move_y, ball = [], [], [], [], [], []
new_ball(5)
move_ball()

"""sets n moving squares"""
x_sq, y_sq, side, sq_move_x, sq_move_y, square = [], [], [], [], [], []
new_square(5)
move_square()

"""function for count points"""
canv.bind('<Button-1>', click)

mainloop()
