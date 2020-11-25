# !/usr/bin/python3
from tkinter import *

from tkinter import messagebox
import random
seed = random.randint(0,10000000)
print(seed)
random.seed(seed)
top = Tk()
SIZE = 500
LINES_COUNT = 10

C = Canvas(top, bg = "#000000", height = SIZE, width = SIZE)
coords = None
colors = [random.randint(0, 255) for i in range(10)]

def intToHex(number):
    hexadecimal = hex(number)[2:]
    if len(hexadecimal) == 1:
        return '0' + hexadecimal
    else:
        return hexadecimal

def hexCodeFromRgb(red, green, blue):
    hexRed = intToHex(red)
    hexGreen = intToHex(green)
    hexBlue = intToHex(blue)
    return f'#{hexRed}{hexGreen}{hexBlue}'

def draw_symmetricLines(start_x, start_y, end_x, end_y, color):
    C.create_line(start_x, start_y, end_x, end_y, fill=color)
    C.create_line(SIZE - start_x, SIZE - start_y, SIZE - end_x, SIZE - end_y, fill=color)
    C.create_line(SIZE - start_x, start_y, SIZE - end_x, end_y, fill=color)
    C.create_line(start_x, SIZE - start_y, end_x, SIZE - end_y, fill=color)

def generate_random_coords():
    random_coords = []
    for i in range(LINES_COUNT):
        object_coords = [
            random.randint(0,500),
            random.randint(0,500),
            random.randint(0,500),
            random.randint(0,500),
        ]
        random_coords.append(object_coords)
    return random_coords

def update_coords():
    for i in range(LINES_COUNT):
        object_coords = coords[i]
        for j in range(len(object_coords)):
            object_coords[j] += 1
            if object_coords[j] >= SIZE:
                object_coords[j] = 0

def redraw():
    C.delete('all')
    for i in range(LINES_COUNT):
        object_coords = coords[i]
        draw_symmetricLines(
            object_coords[0],
            object_coords[1],
            object_coords[2],
            object_coords[3],
            hexCodeFromRgb(colors[i], 0, 0),
        )
    update_coords()
    top.after(20, redraw)

coords = generate_random_coords()
C.pack()
redraw()
top.mainloop()

