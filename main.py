from window import Window
from shapes import Point, Line

def main():
    win = Window(800,600)

    line1 = Line(Point(40,50),Point(500,50))
    line2 = Line(Point(40,500),Point(500,500))
    line3 = Line(Point(172,578),Point(767,226))

    win.draw_line(line1, "black")
    win.draw_line(line2, "red")
    win.draw_line(line3, "green")

    win.wait_for_close()

    
main()