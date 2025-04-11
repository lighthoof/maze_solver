from tkinter import Tk, BOTH, Canvas

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line():
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def draw(self, canvas, color):
        canvas.create_line(self.start.x, self.start.y, self.end.x, self.end.y, fill=color, width=2)

    