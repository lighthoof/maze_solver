class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line():
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def draw(self, canvas, color="black"):
        canvas.create_line(
            self.start.x, self.start.y, self.end.x, self.end.y, fill=color, width=2
        )

class Cell():
    def __init__(self, point1, point2, win):
        self._x1 = point1.x
        self._y1 = point1.y
        self._x2 = point2.x
        self._y2 = point2.y
        self.win = win

        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
    
    def draw(self):
        if self.win.canvas is None: return
        if self.has_left_wall:
            self.draw_line(self._x1, self._y1, self._x1, self._y2)
        else:
            self.draw_line(self._x1, self._y1+1, self._x1, self._y2-1, "#d9d9d9")
        if self.has_right_wall:
            self.draw_line(self._x2, self._y1, self._x2, self._y2)
        else:
            self.draw_line(self._x2, self._y1+1, self._x2, self._y2-1, "#d9d9d9")
        if self.has_top_wall:
            self.draw_line(self._x1, self._y1, self._x2, self._y1)
        else:
            self.draw_line(self._x1+1, self._y1, self._x2-1, self._y1, "#d9d9d9")
        if self.has_bottom_wall:
            self.draw_line(self._x1, self._y2, self._x2, self._y2)
        else:
            self.draw_line(self._x1+1, self._y2, self._x2-2, self._y2, "#d9d9d9")

    def draw_line(self, x1, y1, x2, y2, color="black"):
        start = Point(x1, y1)
        end = Point(x2, y2)
        line = Line(start, end)
        line.draw(self.win.canvas, color)

    def draw_move(self, to_cell, canvas, undo=False):
        start = Point((self._x1 + self._x2) // 2, (self._y1 + self._y2) // 2)
        end = Point((to_cell._x1 + to_cell._x2) // 2, (to_cell._y1 + to_cell._y2) // 2)
        line = Line(start, end)
        if undo:
            line.draw(canvas, "gray")
        else:
            line.draw(canvas, "red")