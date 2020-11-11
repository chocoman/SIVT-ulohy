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

def hexCodeFromRgb(red, green, blue):
    hexRed = hex(red)[2:]
    hexGreen = hex(green)[2:]
    hexBlue = hex(blue)[2:]
    return f'#{hexRed}{hexGreen}{hexBlue}'

def draw_symmetricLines(start_x, start_y, end_x, end_y, color):
    line = C.create_line(start_x, start_y, end_x, end_y, fill=color)
    line = C.create_line(SIZE - start_x, SIZE - start_y, SIZE - end_x, SIZE - end_y, fill=color)
    line = C.create_line(SIZE - start_x, start_y, SIZE - end_x, end_y, fill=color)
    line = C.create_line(start_x, SIZE - start_y, end_x, SIZE - end_y, fill=color)

print(hexCodeFromRgb(0, 255, 0))
for i in range(10):
    draw_symmetricLines(
        random.randint(0,500),
        random.randint(0,500),
        random.randint(0,500),
        random.randint(0,500),
        'white',
    )
C.pack()
top.mainloop()