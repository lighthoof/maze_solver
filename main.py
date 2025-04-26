from window import Window
from shapes import Point, Cell
from maze import Maze

def main():
    num_cols = 12
    num_rows = 10
    size_h = 50
    size_v = 50
    win = Window(num_cols * size_h + 2, num_rows * size_v + 2)
    #win = Window(1200, 900)
    maze = Maze(0, 0, num_cols, num_rows, size_h, size_v, win)
    maze._break_entrance_and_exit()
    maze._break_walls_r()
    maze.solve()
    #cell1 = Cell(Point(50,50),Point(100,100),win)
    #cell1.has_right_wall = False
    #cell2 = Cell(Point(100,50),Point(150,100),win)
    #cell2.has_left_wall = False
    #cell2.has_bottom_wall = False
    #cell3 = Cell(Point(100,100),Point(150,150),win)
    #cell3.has_top_wall = False#

    #win.draw_cell(cell1)
    #win.draw_cell(cell2)
    #win.draw_cell(cell3)

    #win.draw_move(cell1, cell2)
    #win.draw_move(cell2, cell3)

    win.wait_for_close()

    
main()