import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_row(self):
        num_cols = 12
        num_rows = 1
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_column(self):
        num_cols = 1
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_no_cells(self):
        num_cols = 0
        num_rows = 0
        
        with self.assertRaises(ValueError) as context:
            m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertTrue("Incorrect number of rows or columns" in str(context.exception))

    def test_start_and_finish(self):
        m1 = Maze(0, 0, 12, 12, 10, 10)
        m1._break_entrance_and_exit()
        self.assertFalse(m1._cells[0][0].has_top_wall)
        self.assertFalse(m1._cells[-1][-1].has_bottom_wall)

    def test_reset_cells_visited(self):
        m1 = Maze(0, 0, 12, 12, 10, 10)
        m1._break_walls_r()
        m1._reset_cells_visited()
        for column in m1._cells:
            for cell in column:
                self.assertFalse
if __name__ == "__main__":
    unittest.main()