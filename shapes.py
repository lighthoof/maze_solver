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

class Cell():
    def __init__(self, point1, point2):
        self._x1 = point1.x
        self._y1 = point1.y
        self._x2 = point2.x
        self._y2 = point2.y
        self._win = False

        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
    
    def draw(self, canvas, color):
        if self.has_left_wall:
            start = Point(self._x1, self._y1)
            end = Point(self._x1, self._y2)
            line = Line(start, end)
            line.draw(canvas, color)
        if self.has_right_wall:
            start = Point(self._x2, self._y1)
            end = Point(self._x2, self._y2)
            line = Line(start, end)
            line.draw(canvas, color)
        if self.has_top_wall:
            start = Point(self._x1, self._y1)
            end = Point(self._x2, self._y1)
            line = Line(start, end)
            line.draw(canvas, color)
        if self.has_bottom_wall:
            start = Point(self._x1, self._y2)
            end = Point(self._x2, self._y2)
            line = Line(start, end)
            line.draw(canvas, color)