from window import Window
from shapes import Point, Cell

def main():
    win = Window(800,600)

    cell1 = Cell(Point(50,50),Point(100,100))
    cell1.has_top_wall = False
    cell2 = Cell(Point(150,150),Point(200,200))
    cell2.has_left_wall = False
    cell3 = Cell(Point(700,500),Point(750,550))
    cell3.has_bottom_wall = False
    cell3.has_right_wall = False

    win.draw_cell(cell1, "black")
    win.draw_cell(cell2, "red")
    win.draw_cell(cell3, "green")

    win.wait_for_close()

    
main()