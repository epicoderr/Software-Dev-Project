import unittest
from game.minesweeper import Minesweeper

class TestSolitaire(unittest.TestCase):

    def setUp(self):
        self.game = Minesweeper()
        self.game.create_puzzle()

    def test_initial_board_has_forty_mines(self):
        # Counts all the mines on the board and sees if its exactly 40
        tile_count = sum(1 for row in self.game.board for tile in row if tile == "2")
        self.assertEqual(tile_count, self.game.mines)