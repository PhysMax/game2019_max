from tkinter import *
from random import randrange as rnd, choice
import math
import time

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


def new_ball(k):
    global x, y, r, move_x, move_y, ball
    x.append(rnd(100, 700))
    y.append(rnd(100, 500))
    r.append(rnd(30, 50))
    move_x.append(rnd(-10, 10))
    move_y.append(rnd(-10, 10))
    ball.append(canv.create_oval(x[k] - r[k], y[k] - r[k], x[k] + r[k], y[k] + r[k], fill=choice(colors), width=0))


score = [0, 0]


def click(event):
    for i in range(50):
        if math.sqrt((x[i] - event.x) ** 2 + (y[i] - event.y) ** 2) <= r[i]:
            score[0] += 1
    score[1] += 1
    print(score)


global x, y, r, move_x, move_y, ball

x = []
y = []
r = []
move_x = []
move_y = []
ball = []


for l in range(50):
    new_ball(l)
move_ball()

canv.bind('<Button-1>', click)
mainloop()
