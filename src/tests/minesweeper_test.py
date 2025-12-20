import unittest
from game.minesweeper import Minesweeper
from unittest.mock import patch

class TestMinesweeper(unittest.TestCase):

    def setUp(self):
        self.game = Minesweeper()
    
    def set_mines_for_testing(self, size, positions):
        # helper for testing the state of the board
        self.game = Minesweeper(size=size)
        self.game.new_game()
        for r, c in positions:
            if 0 <= r < self.game.size and 0 <= c < self.game.size:
                self.game.board.grid[r][c].is_mine = True
        self.game.mines = len(positions)
        self.game.board.number_cells()
        self.game.first_click = False

    def test_initial_board_has_forty_mines(self):
        # Counts all the mines on the board and sees if its exactly 40
        self.game.reveal_cell(0,0)

        mine_count = sum(1 for row in self.game.board.grid for tile in row if tile.is_mine)
        self.assertEqual(mine_count, self.game.mines)

    def test_reveal_cell(self):
        self.game.reveal_cell(1,1)
        self.assertTrue(self.game.board.grid[1][1].is_revealed)

    def test_toggle_flag(self):
        self.game.toggle_flag(1,1)
        self.assertFalse(self.game.board.grid[1][1].is_flagged)
        self.game.first_click = False
        self.game.toggle_flag(1,1)
        self.assertTrue(self.game.board.grid[1][1].is_flagged)
        self.game.toggle_flag(1,1)
        self.assertFalse(self.game.board.grid[1][1].is_flagged)
    
    def test_cell_with_no_neighbors(self):
        # 5x5 board with the center cell having no mine neighbors
        positions = [(0,0), (4,4)]
        self.set_mines_for_testing(size=5, positions=positions)

        self.assertFalse(self.game.board.grid[2][2].is_mine)
        self.assertEqual(self.game.board.grid[2][2].neighbor_count, 0)

    def test_cell_with_eight_neighbors(self):
        # 3x3 board with the center cell having eight
        positions = [(0,0), (0,1), (0,2), (1,0), (1,2), (2,0), (2,1), (2,2)]
        self.set_mines_for_testing(size=3, positions=positions)

        self.assertFalse(self.game.board.grid[1][1].is_mine)
        self.assertEqual(self.game.board.grid[1][1].neighbor_count, 8)
    
    def test_new_game(self):
        # Tests that new_game initializes board correctly
        game = Minesweeper()
        game.new_game()
        
        self.assertEqual(len(game.board.grid), game.size)
        self.assertEqual(len(game.board.grid[0]), game.size)

        self.assertTrue(all(cell.is_revealed == False for row in game.board.grid for cell in row))
    
    def test_reveal_adjacent_cells(self):
        # Tests that revealing a cell with no adjacent mines reveal other with none
        positions = [(2,0), (2,1), (2,2)]
        self.set_mines_for_testing(size=3, positions=positions)
        self.game.reveal_cell(0,0)

        self.assertTrue(self.game.board.grid[0][0].is_revealed)
        self.assertTrue(self.game.board.grid[0][1].is_revealed)
        self.assertTrue(self.game.board.grid[0][2].is_revealed)
        self.assertTrue(self.game.board.grid[1][0].is_revealed)
        self.assertTrue(self.game.board.grid[1][1].is_revealed)
        self.assertTrue(self.game.board.grid[1][2].is_revealed)
        self.assertFalse(self.game.board.grid[2][0].is_revealed)
        self.assertFalse(self.game.board.grid[2][1].is_revealed)
        self.assertFalse(self.game.board.grid[2][2].is_revealed)

    def test_reveal_mine_ends_game(self):
        # Tests that game_over is applied once a mine is hit
        self.set_mines_for_testing(size=3, positions=[(1, 1)])

        self.game.reveal_cell(1, 1)

        self.assertTrue(self.game.game_over)
        self.assertTrue(self.game.board.grid[1][1].is_revealed)

    def test_winning_game_prints_message(self):
        # Tests that winning game is recognized and message printed
        self.set_mines_for_testing(size=2, positions=[(0, 0)])

        with patch("builtins.print") as mock_print:
            self.game.reveal_cell(0, 1)
            self.game.reveal_cell(1, 0)
            self.game.reveal_cell(1, 1)

        mock_print.assert_called_with("All safe cells revealed!")

    def test_out_of_bounds_inputs(self):
        """Tests that reveal_cell and toggle_flag handle invalid coordinates gracefully."""
        self.game.reveal_cell(-1, 0)
        self.game.reveal_cell(0, -1)
        self.game.reveal_cell(self.game.size, self.game.size)
        self.assertTrue(self.game.first_click) # First click should still be true after no reveal

        self.game.first_click = False
        
        try:
            self.game.toggle_flag(-1, 5)
            self.game.toggle_flag(5, self.game.size)
        except IndexError:
            self.fail("toggle_flag raised IndexError for out-of-bounds coordinates!")
