# !/usr/bin/python3
from tkinter import *

from tkinter import messagebox
import random
seed = random.randint(0,10000000)
print(seed)
random.seed(seed)
top = Tk()
SIZE = 500
C = Canvas(top, bg = "#000000", height = SIZE, width = SIZE)

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


for i in range(10):
    draw_symmetricLines(
        random.randint(0,500),
        random.randint(0,500),
        random.randint(0,500),
        random.randint(0,500),
        hexCodeFromRgb(random.randint(0, 255), 0, 0),
    )
C.pack()
top.mainloop()
