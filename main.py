from window import Window
from shapes import Point, Cell

def main():
    win = Window(800,600)

    cell1 = Cell(Point(50,50),Point(100,100))
    cell1.has_right_wall = False
    cell2 = Cell(Point(100,50),Point(150,100))
    cell2.has_left_wall = False
    cell2.has_bottom_wall = False
    cell3 = Cell(Point(100,100),Point(150,150))
    cell3.has_top_wall = False

    win.draw_cell(cell1)
    win.draw_cell(cell2)
    win.draw_cell(cell3)

    win.draw_move(cell1, cell2)
    win.draw_move(cell2, cell3)

    win.wait_for_close()

    
main()