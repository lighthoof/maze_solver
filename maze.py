from shapes import Cell, Point

class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._create_cells()
    
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
                if i != j and i == 0:
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
        
        self._draw_cells(self, i, j)

    def _draw_cells(self, i, j):
        pass