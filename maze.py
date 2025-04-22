from shapes import Cell, Point
import time
import random

class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win = None,
        seed = None
    ):
        self.x1 = x1
        self.y1 = y1
        if num_rows == 0 or num_cols == 0:
            raise ValueError("Incorrect number of rows or columns")
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._create_cells()
        if seed is not None:
            random.seed(seed)
    
    def _create_cells(self):
        self._cells = []
        for i in range(self.num_cols):
            column = []
            for j in range(self.num_rows):
                if i == j and i == 0:
                    column.append(
                        Cell(
                            Point(0,0),Point(self.cell_size_x,self.cell_size_y)
                            )
                        )
                elif i != j and i == 0:
                    column.append(
                        Cell(
                            Point(0,0),Point((i+1)*self.cell_size_x, (j+1)*self.cell_size_y)
                            )
                        )
                else:    
                    column.append(
                        Cell(
                            Point(i * self.cell_size_x, j * self.cell_size_y),
                            Point((i+1)*self.cell_size_x, (j+1)*self.cell_size_y)
                            )
                        )
            self._cells.append(column)
                    
        for column in self._cells:
            for cell in column:
                cell.draw()
                self._animate()

    def _animate(self):
        if self.win is None: 
            return
        else: 
            self.win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[0][0].draw()
        self._cells[-1][-1].has_bottom_wall = False
        self._cells[-1][-1].draw()

    def _break_walls(self):
        pass

    def _break_Walls_r(self, i, j):
        pass