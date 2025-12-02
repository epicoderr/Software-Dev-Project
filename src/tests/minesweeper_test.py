import unittest
from game.minesweeper import Minesweeper

class TestMinesweeper(unittest.TestCase):

    def setUp(self):
        self.game = Minesweeper()
        self.game.create_board()
    
    def set_mines_for_testing(self, size, positions):
        # helper for testing the state of the board
        self.game = Minesweeper(size=size)
        self.game.create_board()
        for r, c in positions:
            if 0 <= r < self.game.size and 0 <= c < self.game.size:
                self.game.board[r][c]["isMine"] = True
        self.game.number_cells()

    def test_initial_board_has_forty_mines(self):
        # Counts all the mines on the board and sees if its exactly 40
        self.game.create_puzzle()
        self.game.number_cells()

        tile_count = sum(1 for row in self.game.board for tile in row if tile["isMine"])
        self.assertEqual(tile_count, self.game.mines)

    def test_reveal_cell(self):
        self.game.reveal_cell(1,1)
        self.assertTrue(self.game.board[1][1]["isRevealed"])

    def test_toggle_flag(self):
        self.game.toggle_flag(1,1)
        self.assertTrue(self.game.board[1][1]["isFlagged"])
        self.game.toggle_flag(1,1)
        self.assertFalse(self.game.board[1][1]["isFlagged"])
    
    def test_cell_with_no_neighbors(self):
        # 5x5 board with the center cell having no mine neighbors
        positions = [(0,0), (4,4)]
        self.set_mines_for_testing(size=5, positions=positions)

        self.assertFalse(self.game.board[2][2]["isMine"])
        self.assertEqual(self.game.board[2][2]["neighborCount"], 0)

    def test_cell_with_eight_neighbors(self):
        # 3x3 board with the center cell having eight
        positions = [(0,0), (0,1), (0,2), (1,0), (1,2), (2,0), (2,1), (2,2)]
        self.set_mines_for_testing(size=3, positions=positions)

        self.assertFalse(self.game.board[1][1]["isMine"])
        self.assertEqual(self.game.board[1][1]["neighborCount"], 8)
    
    def test_new_game(self):
        # Tests that new_game initializes board correctly
        game = Minesweeper()
        game.new_game()
        
        self.assertEqual(len(game.board), game.size)
        self.assertEqual(len(game.board[0]), game.size)

        self.assertTrue(all(cell["isRevealed"] == False for row in game.board for cell in row))
    
    def test_reveal_adjacent_cells(self):
        # Tests that revealing a cell with no adjacent mines reveal other with none
        positions = [(2,0), (2,1), (2,2)]
        self.set_mines_for_testing(size=3, positions=positions)
        self.game.reveal_cell(0,0)

        self.assertTrue(self.game.board[0][0]["isRevealed"])
        self.assertTrue(self.game.board[0][1]["isRevealed"])
        self.assertTrue(self.game.board[0][2]["isRevealed"])
        self.assertTrue(self.game.board[1][0]["isRevealed"])
        self.assertTrue(self.game.board[1][1]["isRevealed"])
        self.assertTrue(self.game.board[1][2]["isRevealed"])
        self.assertFalse(self.game.board[2][0]["isRevealed"])
        self.assertFalse(self.game.board[2][1]["isRevealed"])
        self.assertFalse(self.game.board[2][2]["isRevealed"])

    