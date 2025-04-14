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
    def __init__(self, point1, point2):
        self._x1 = point1.x
        self._y1 = point1.y
        self._x2 = point2.x
        self._y2 = point2.y

        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
    
    def draw(self, canvas):
        if self.has_left_wall:
            start = Point(self._x1, self._y1)
            end = Point(self._x1, self._y2)
            line = Line(start, end)
            line.draw(canvas)
        if self.has_right_wall:
            start = Point(self._x2, self._y1)
            end = Point(self._x2, self._y2)
            line = Line(start, end)
            line.draw(canvas)
        if self.has_top_wall:
            start = Point(self._x1, self._y1)
            end = Point(self._x2, self._y1)
            line = Line(start, end)
            line.draw(canvas)
        if self.has_bottom_wall:
            start = Point(self._x1, self._y2)
            end = Point(self._x2, self._y2)
            line = Line(start, end)
            line.draw(canvas)

    def draw_move(self, to_cell, canvas, undo=False):
        start = Point((self._x1 + self._x2) // 2, (self._y1 + self._y2) // 2)
        end = Point((to_cell._x1 + to_cell._x2) // 2, (to_cell._y1 + to_cell._y2) // 2)
        line = Line(start, end)
        if undo:
            line.draw(canvas, "gray")
        else:
            line.draw(canvas, "red")