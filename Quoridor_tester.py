# Author: Kelsey Schmidt
# Date: 7-29-21
# Description:  # Testing file for QuoridorGame.py, containing unit tests.

import unittest
from Quoridor import QuoridorGame

class TestQuoridorGame(unittest.TestCase):

    """
    Contains unit tests for the Quoridor file.
    """

    def test_QuoridorGame_get_board(self):
        """
        Tests QuoridorGame get_board.
        """
        q = QuoridorGame()
        result = q.get_board()
        # this is only hard coded here for the purpose of the test
        self.assertEqual(result, [
            ['. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. '],
            ['| ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', 'P1', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '| '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['| ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '| '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['| ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '| '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['| ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '| '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['| ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '| '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['| ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '| '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['| ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '| '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['| ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '| '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['| ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', 'P2', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '| '],
            ['. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ']
        ])

    def test_QuoridorGame_set_board(self):
        """
        Tests QuoridorGame set_board.
        """
        q = QuoridorGame()
        board = [0, 1, 2, 3]
        q.set_board(board)
        result = q.get_board()
        self.assertEqual(result, [0, 1, 2, 3])

    def test_QuoridorGame_get_coords_dict(self):
        """
        Tests QuoridorGame get_coords_dict.
        """
        q = QuoridorGame()
        result = q.get_coords_dict()
        # this is only hard coded here for the purpose of the test
        self.assertEqual(result, {(0, 0): '. ', (1, 0): '. ', (2, 0): '. ', (3, 0): '. ', (4, 0): '. ', (5, 0): '. ',
                                  (6, 0): '. ', (7, 0): '. ', (8, 0): '. ', (9, 0): '. ', (0, 1): '. ', (1, 1): '. ',
                                  (2, 1): '. ', (3, 1): '. ', (4, 1): '. ', (5, 1): '. ', (6, 1): '. ', (7, 1): '. ',
                                  (8, 1): '. ', (9, 1): '. ', (0, 2): '. ', (1, 2): '. ', (2, 2): '. ', (3, 2): '. ',
                                  (4, 2): '. ', (5, 2): '. ', (6, 2): '. ', (7, 2): '. ', (8, 2): '. ', (9, 2): '. ',
                                  (0, 3): '. ', (1, 3): '. ', (2, 3): '. ', (3, 3): '. ', (4, 3): '. ', (5, 3): '. ',
                                  (6, 3): '. ', (7, 3): '. ', (8, 3): '. ', (9, 3): '. ', (0, 4): '. ', (1, 4): '. ',
                                  (2, 4): '. ', (3, 4): '. ', (4, 4): '. ', (5, 4): '. ', (6, 4): '. ', (7, 4): '. ',
                                  (8, 4): '. ', (9, 4): '. ', (0, 5): '. ', (1, 5): '. ', (2, 5): '. ', (3, 5): '. ',
                                  (4, 5): '. ', (5, 5): '. ', (6, 5): '. ', (7, 5): '. ', (8, 5): '. ', (9, 5): '. ',
                                  (0, 6): '. ', (1, 6): '. ', (2, 6): '. ', (3, 6): '. ', (4, 6): '. ', (5, 6): '. ',
                                  (6, 6): '. ', (7, 6): '. ', (8, 6): '. ', (9, 6): '. ', (0, 7): '. ', (1, 7): '. ',
                                  (2, 7): '. ', (3, 7): '. ', (4, 7): '. ', (5, 7): '. ', (6, 7): '. ', (7, 7): '. ',
                                  (8, 7): '. ', (9, 7): '. ', (0, 8): '. ', (1, 8): '. ', (2, 8): '. ', (3, 8): '. ',
                                  (4, 8): '. ', (5, 8): '. ', (6, 8): '. ', (7, 8): '. ', (8, 8): '. ', (9, 8): '. ',
                                  (0, 9): '. ', (1, 9): '. ', (2, 9): '. ', (3, 9): '. ', (4, 9): '. ', (5, 9): '. ',
                                  (6, 9): '. ', (7, 9): '. ', (8, 9): '. ', (9, 9): '. '})

    def test_QuoridorGame_get_horiz_edges_dict(self):
        """
        Tests QuoridorGame get_horiz_edges_dict.
        """
        q = QuoridorGame()
        result = q.get_horiz_edges_dict()
        # this is only hard coded here for the purpose of the test
        self.assertEqual(result, {(0, 0): '__', (1, 0): '__', (2, 0): '__', (3, 0): '__', (4, 0): '__', (5, 0): '__',
                                  (6, 0): '__', (7, 0): '__', (8, 0): '__', (0, 1): '  ', (1, 1): '  ', (2, 1): '  ',
                                  (3, 1): '  ', (4, 1): '  ', (5, 1): '  ', (6, 1): '  ', (7, 1): '  ', (8, 1): '  ',
                                  (0, 2): '  ', (1, 2): '  ', (2, 2): '  ', (3, 2): '  ', (4, 2): '  ', (5, 2): '  ',
                                  (6, 2): '  ', (7, 2): '  ', (8, 2): '  ', (0, 3): '  ', (1, 3): '  ', (2, 3): '  ',
                                  (3, 3): '  ', (4, 3): '  ', (5, 3): '  ', (6, 3): '  ', (7, 3): '  ', (8, 3): '  ',
                                  (0, 4): '  ', (1, 4): '  ', (2, 4): '  ', (3, 4): '  ', (4, 4): '  ', (5, 4): '  ',
                                  (6, 4): '  ', (7, 4): '  ', (8, 4): '  ', (0, 5): '  ', (1, 5): '  ', (2, 5): '  ',
                                  (3, 5): '  ', (4, 5): '  ', (5, 5): '  ', (6, 5): '  ', (7, 5): '  ', (8, 5): '  ',
                                  (0, 6): '  ', (1, 6): '  ', (2, 6): '  ', (3, 6): '  ', (4, 6): '  ', (5, 6): '  ',
                                  (6, 6): '  ', (7, 6): '  ', (8, 6): '  ', (0, 7): '  ', (1, 7): '  ', (2, 7): '  ',
                                  (3, 7): '  ', (4, 7): '  ', (5, 7): '  ', (6, 7): '  ', (7, 7): '  ', (8, 7): '  ',
                                  (0, 8): '  ', (1, 8): '  ', (2, 8): '  ', (3, 8): '  ', (4, 8): '  ', (5, 8): '  ',
                                  (6, 8): '  ', (7, 8): '  ', (8, 8): '  ', (0, 9): '__', (1, 9): '__', (2, 9): '__',
                                  (3, 9): '__', (4, 9): '__', (5, 9): '__', (6, 9): '__', (7, 9): '__', (8, 9): '__'})

    def test_QuoridorGame_set_horiz_edges_dict(self):
        """
        Tests QuoridorGame set_horiz_edges_dict.
        """
        q = QuoridorGame()
        q.set_horiz_edges_dict({"a":1})
        result = q.get_horiz_edges_dict()
        self.assertEqual(result, {"a":1})

    def test_QuoridorGame_get_vert_edges_dict(self):
        """
        Tests QuoridorGame get_vert_edges_dict.
        """
        q = QuoridorGame()
        result = q.get_vert_edges_dict()
        # this is only hard coded here for the purpose of the test
        self.assertEqual(result, {(0, 0): '| ', (1, 0): '  ', (2, 0): '  ', (3, 0): '  ', (4, 0): '  ', (5, 0): '  ',
                                  (6, 0): '  ', (7, 0): '  ', (8, 0): '  ', (9, 0): '| ', (0, 1): '| ', (1, 1): '  ',
                                  (2, 1): '  ', (3, 1): '  ', (4, 1): '  ', (5, 1): '  ', (6, 1): '  ', (7, 1): '  ',
                                  (8, 1): '  ', (9, 1): '| ', (0, 2): '| ', (1, 2): '  ', (2, 2): '  ', (3, 2): '  ',
                                  (4, 2): '  ', (5, 2): '  ', (6, 2): '  ', (7, 2): '  ', (8, 2): '  ', (9, 2): '| ',
                                  (0, 3): '| ', (1, 3): '  ', (2, 3): '  ', (3, 3): '  ', (4, 3): '  ', (5, 3): '  ',
                                  (6, 3): '  ', (7, 3): '  ', (8, 3): '  ', (9, 3): '| ', (0, 4): '| ', (1, 4): '  ',
                                  (2, 4): '  ', (3, 4): '  ', (4, 4): '  ', (5, 4): '  ', (6, 4): '  ', (7, 4): '  ',
                                  (8, 4): '  ', (9, 4): '| ', (0, 5): '| ', (1, 5): '  ', (2, 5): '  ', (3, 5): '  ',
                                  (4, 5): '  ', (5, 5): '  ', (6, 5): '  ', (7, 5): '  ', (8, 5): '  ', (9, 5): '| ',
                                  (0, 6): '| ', (1, 6): '  ', (2, 6): '  ', (3, 6): '  ', (4, 6): '  ', (5, 6): '  ',
                                  (6, 6): '  ', (7, 6): '  ', (8, 6): '  ', (9, 6): '| ', (0, 7): '| ', (1, 7): '  ',
                                  (2, 7): '  ', (3, 7): '  ', (4, 7): '  ', (5, 7): '  ', (6, 7): '  ', (7, 7): '  ',
                                  (8, 7): '  ', (9, 7): '| ', (0, 8): '| ', (1, 8): '  ', (2, 8): '  ', (3, 8): '  ',
                                  (4, 8): '  ', (5, 8): '  ', (6, 8): '  ', (7, 8): '  ', (8, 8): '  ', (9, 8): '| '})

    def test_QuoridorGame_set_vert_edges_dict(self):
        """
        Tests QuoridorGame set_vert_edges_dict.
        """
        q = QuoridorGame()
        q.set_vert_edges_dict({"a":1})
        result = q.get_vert_edges_dict()
        self.assertEqual(result, {"a":1})

    def test_QuoridorGame_get_spaces_dict(self):
        """
        Tests QuoridorGame get_spaces_dict.
        """
        q = QuoridorGame()
        result = q.get_spaces_dict()
        # this is only hard coded here for the purpose of the test
        self.assertEqual(result, {(0, 0): '  ', (1, 0): '  ', (2, 0): '  ', (3, 0): '  ', (4, 0): 'P1', (5, 0): '  ',
                                  (6, 0): '  ', (7, 0): '  ', (8, 0): '  ', (0, 1): '  ', (1, 1): '  ', (2, 1): '  ',
                                  (3, 1): '  ', (4, 1): '  ', (5, 1): '  ', (6, 1): '  ', (7, 1): '  ', (8, 1): '  ',
                                  (0, 2): '  ', (1, 2): '  ', (2, 2): '  ', (3, 2): '  ', (4, 2): '  ', (5, 2): '  ',
                                  (6, 2): '  ', (7, 2): '  ', (8, 2): '  ', (0, 3): '  ', (1, 3): '  ', (2, 3): '  ',
                                  (3, 3): '  ', (4, 3): '  ', (5, 3): '  ', (6, 3): '  ', (7, 3): '  ', (8, 3): '  ',
                                  (0, 4): '  ', (1, 4): '  ', (2, 4): '  ', (3, 4): '  ', (4, 4): '  ', (5, 4): '  ',
                                  (6, 4): '  ', (7, 4): '  ', (8, 4): '  ', (0, 5): '  ', (1, 5): '  ', (2, 5): '  ',
                                  (3, 5): '  ', (4, 5): '  ', (5, 5): '  ', (6, 5): '  ', (7, 5): '  ', (8, 5): '  ',
                                  (0, 6): '  ', (1, 6): '  ', (2, 6): '  ', (3, 6): '  ', (4, 6): '  ', (5, 6): '  ',
                                  (6, 6): '  ', (7, 6): '  ', (8, 6): '  ', (0, 7): '  ', (1, 7): '  ', (2, 7): '  ',
                                  (3, 7): '  ', (4, 7): '  ', (5, 7): '  ', (6, 7): '  ', (7, 7): '  ', (8, 7): '  ',
                                  (0, 8): '  ', (1, 8): '  ', (2, 8): '  ', (3, 8): '  ', (4, 8): 'P2', (5, 8): '  ',
                                  (6, 8): '  ', (7, 8): '  ', (8, 8): '  '})

    def test_QuoridorGame_set_spaces_dict(self):
        """
        Tests QuoridorGame set_spaces_dict.
        """
        q = QuoridorGame()
        q.set_spaces_dict({"a":1})
        result = q.get_spaces_dict()
        self.assertEqual(result, {"a":1})

    def test_QuoridorGame_get_game_won(self):
        """
        Tests QuoridorGame get_game_won.
        """
        q = QuoridorGame()
        result = q.get_game_won()
        self.assertFalse(result)

    def test_QuoridorGame_set_game_won(self):
        """
        Tests QuoridorGame set_game_won.
        """
        q = QuoridorGame()
        q.set_game_won(True)
        result = q.get_game_won()
        self.assertTrue(result)

    def test_QuoridorGame_get_winner(self):
        """
        Tests QuoridorGame get_winner.
        """
        q = QuoridorGame()
        result = q.get_winner()
        self.assertEqual(result, None)

    def test_QuoridorGame_set_winner(self):
        """
        Tests QuoridorGame set_winner.
        """
        q = QuoridorGame()
        q.set_winner(1)
        result = q.get_winner()
        self.assertEqual(result, 1)

    def test_QuoridorGame_get_player_turn(self):
        """
        Tests QuoridorGame get_player_turn.
        """
        q = QuoridorGame()
        result = q.get_player_turn()
        self.assertEqual(result, 1)

    def test_QuoridorGame_set_player_turn(self):
        """
        Tests QuoridorGame set_player_turn.
        """
        q = QuoridorGame()
        q.set_player_turn(2)
        result = q.get_player_turn()
        self.assertEqual(result, 2)

    def test_QuoridorGame_amend_board(self):
        """
        Tests QuoridorGame amend_board.
        """
        q = QuoridorGame()
        horiz_edges_dict = {(0, 0): '**', (1, 0): '**', (2, 0): '**', (3, 0): '**', (4, 0): '**', (5, 0): '**',
                                  (6, 0): '**', (7, 0): '**', (8, 0): '**', (0, 1): '  ', (1, 1): '  ', (2, 1): '  ',
                                  (3, 1): '  ', (4, 1): '  ', (5, 1): '  ', (6, 1): '  ', (7, 1): '  ', (8, 1): '  ',
                                  (0, 2): '  ', (1, 2): '  ', (2, 2): '  ', (3, 2): '  ', (4, 2): '  ', (5, 2): '  ',
                                  (6, 2): '  ', (7, 2): '  ', (8, 2): '  ', (0, 3): '  ', (1, 3): '  ', (2, 3): '  ',
                                  (3, 3): '  ', (4, 3): '  ', (5, 3): '  ', (6, 3): '  ', (7, 3): '  ', (8, 3): '  ',
                                  (0, 4): '  ', (1, 4): '  ', (2, 4): '  ', (3, 4): '  ', (4, 4): '  ', (5, 4): '  ',
                                  (6, 4): '  ', (7, 4): '  ', (8, 4): '  ', (0, 5): '  ', (1, 5): '  ', (2, 5): '  ',
                                  (3, 5): '  ', (4, 5): '  ', (5, 5): '  ', (6, 5): '  ', (7, 5): '  ', (8, 5): '  ',
                                  (0, 6): '  ', (1, 6): '  ', (2, 6): '  ', (3, 6): '  ', (4, 6): '  ', (5, 6): '  ',
                                  (6, 6): '  ', (7, 6): '  ', (8, 6): '  ', (0, 7): '  ', (1, 7): '  ', (2, 7): '  ',
                                  (3, 7): '  ', (4, 7): '  ', (5, 7): '  ', (6, 7): '  ', (7, 7): '  ', (8, 7): '  ',
                                  (0, 8): '  ', (1, 8): '  ', (2, 8): '  ', (3, 8): '  ', (4, 8): '  ', (5, 8): '  ',
                                  (6, 8): '  ', (7, 8): '  ', (8, 8): '  ', (0, 9): '**', (1, 9): '**', (2, 9): '**',
                                  (3, 9): '**', (4, 9): '**', (5, 9): '**', (6, 9): '**', (7, 9): '**', (8, 9): '**'}
        vert_edges_dict = {(0, 0): '@ ', (1, 0): '  ', (2, 0): '  ', (3, 0): '  ', (4, 0): '  ', (5, 0): '  ',
                                  (6, 0): '  ', (7, 0): '  ', (8, 0): '  ', (9, 0): '@ ', (0, 1): '@ ', (1, 1): '  ',
                                  (2, 1): '  ', (3, 1): '  ', (4, 1): '  ', (5, 1): '  ', (6, 1): '  ', (7, 1): '  ',
                                  (8, 1): '  ', (9, 1): '@ ', (0, 2): '@ ', (1, 2): '  ', (2, 2): '  ', (3, 2): '  ',
                                  (4, 2): '  ', (5, 2): '  ', (6, 2): '  ', (7, 2): '  ', (8, 2): '  ', (9, 2): '@ ',
                                  (0, 3): '@ ', (1, 3): '  ', (2, 3): '  ', (3, 3): '  ', (4, 3): '  ', (5, 3): '  ',
                                  (6, 3): '  ', (7, 3): '  ', (8, 3): '  ', (9, 3): '@ ', (0, 4): '@ ', (1, 4): '  ',
                                  (2, 4): '  ', (3, 4): '  ', (4, 4): '  ', (5, 4): '  ', (6, 4): '  ', (7, 4): '  ',
                                  (8, 4): '  ', (9, 4): '@ ', (0, 5): '@ ', (1, 5): '  ', (2, 5): '  ', (3, 5): '  ',
                                  (4, 5): '  ', (5, 5): '  ', (6, 5): '  ', (7, 5): '  ', (8, 5): '  ', (9, 5): '@ ',
                                  (0, 6): '@ ', (1, 6): '  ', (2, 6): '  ', (3, 6): '  ', (4, 6): '  ', (5, 6): '  ',
                                  (6, 6): '  ', (7, 6): '  ', (8, 6): '  ', (9, 6): '@ ', (0, 7): '@ ', (1, 7): '  ',
                                  (2, 7): '  ', (3, 7): '  ', (4, 7): '  ', (5, 7): '  ', (6, 7): '  ', (7, 7): '  ',
                                  (8, 7): '  ', (9, 7): '@ ', (0, 8): '@ ', (1, 8): '  ', (2, 8): '  ', (3, 8): '  ',
                                  (4, 8): '  ', (5, 8): '  ', (6, 8): '  ', (7, 8): '  ', (8, 8): '  ', (9, 8): '@ '}
        spaces_dict = {(0, 0): 'b ', (1, 0): 'b ', (2, 0): 'b ', (3, 0): 'b ', (4, 0): 'P1', (5, 0): 'b ',
                                  (6, 0): 'b ', (7, 0): 'b ', (8, 0): 'b ', (0, 1): 'b ', (1, 1): 'b ', (2, 1): 'b ',
                                  (3, 1): 'b ', (4, 1): 'b ', (5, 1): 'b ', (6, 1): 'b ', (7, 1): 'b ', (8, 1): 'b ',
                                  (0, 2): 'b ', (1, 2): 'b ', (2, 2): 'b ', (3, 2): 'b ', (4, 2): 'b ', (5, 2): 'b ',
                                  (6, 2): 'b ', (7, 2): 'b ', (8, 2): 'b ', (0, 3): 'b ', (1, 3): 'b ', (2, 3): 'b ',
                                  (3, 3): 'b ', (4, 3): 'b ', (5, 3): 'b ', (6, 3): 'b ', (7, 3): 'b ', (8, 3): 'b ',
                                  (0, 4): 'b ', (1, 4): 'b ', (2, 4): 'b ', (3, 4): 'b ', (4, 4): 'b ', (5, 4): 'b ',
                                  (6, 4): 'b ', (7, 4): 'b ', (8, 4): 'b ', (0, 5): 'b ', (1, 5): 'b ', (2, 5): 'b ',
                                  (3, 5): 'b ', (4, 5): 'b ', (5, 5): 'b ', (6, 5): 'b ', (7, 5): 'b ', (8, 5): 'b ',
                                  (0, 6): 'b ', (1, 6): 'b ', (2, 6): 'b ', (3, 6): 'b ', (4, 6): 'b ', (5, 6): 'b ',
                                  (6, 6): 'b ', (7, 6): 'b ', (8, 6): 'b ', (0, 7): 'b ', (1, 7): 'b ', (2, 7): 'b ',
                                  (3, 7): 'b ', (4, 7): 'b ', (5, 7): 'b ', (6, 7): 'b ', (7, 7): 'b ', (8, 7): 'b ',
                                  (0, 8): 'b ', (1, 8): 'b ', (2, 8): 'b ', (3, 8): 'b ', (4, 8): 'P2', (5, 8): 'b ',
                                  (6, 8): 'b ', (7, 8): 'b ', (8, 8): 'b '}
        q.set_horiz_edges_dict(horiz_edges_dict)
        q.set_vert_edges_dict(vert_edges_dict)
        q.set_spaces_dict(spaces_dict)
        q.amend_board()
        result = q.get_board()
        self.assertEqual(result, [
            ['. ', '**', '. ', '**', '. ', '**', '. ', '**', '. ', '**', '. ', '**', '. ', '**', '. ', '**', '. ', '**', '. '],
            ['@ ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'P1', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '@ '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['@ ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '@ '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['@ ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '@ '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['@ ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '@ '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['@ ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '@ '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['@ ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '@ '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['@ ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '@ '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['@ ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '@ '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['@ ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'P2', '  ', 'b ', '  ', 'b ', '  ', 'b ', '  ', 'b ', '@ '],
            ['. ', '**', '. ', '**', '. ', '**', '. ', '**', '. ', '**', '. ', '**', '. ', '**', '. ', '**', '. ', '**', '. ']
        ])

    def test_QuoridorGame_amend_horiz_edges_dict(self):
        """
        Tests QuoridorGame amend_horiz_edges_dict.
        """
        q = QuoridorGame()
        q.amend_horiz_edges_dict((0,0), "**")
        q.amend_board()
        result = q.get_board()
        self.assertEqual(result, [
            ['. ', '**', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. '],
            ['| ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', 'P1', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '| '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['| ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '| '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['| ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '| '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['| ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '| '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['| ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '| '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['| ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '| '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['| ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '| '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['| ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '| '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['| ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', 'P2', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '| '],
            ['. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ']
        ])

    def test_QuoridorGame_amend_vert_edges_dict(self):
        """
        Tests QuoridorGame amend_vert_edges_dict.
        """
        q = QuoridorGame()
        q.amend_vert_edges_dict((0,0), "f ")
        q.amend_board()
        result = q.get_board()
        self.assertEqual(result, [
            ['. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. '],
            ['f ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', 'P1', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '| '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['| ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '| '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['| ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '| '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['| ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '| '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['| ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '| '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['| ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '| '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['| ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '| '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['| ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '| '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['| ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', 'P2', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '| '],
            ['. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ']
        ])

    def test_QuoridorGame_amend_spaces_dict(self):
        """
        Tests QuoridorGame amend_spaces_dict.
        """
        q = QuoridorGame()
        q.amend_spaces_dict((0,0), "P3")
        q.amend_board()
        result = q.get_board()
        self.assertEqual(result, [
            ['. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. '],
            ['| ', 'P3', '  ', '  ', '  ', '  ', '  ', '  ', '  ', 'P1', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '| '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['| ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '| '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['| ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '| '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['| ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '| '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['| ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '| '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['| ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '| '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['| ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '| '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['| ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '| '],
            ['. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. ', '  ', '. '],
            ['| ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', 'P2', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '| '],
            ['. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ', '__', '. ']
        ])

    def test_QuoridorGame_is_winner(self):
        """
        Tests QuoridorGame is_winner.
        """
        q = QuoridorGame()
        result = q.is_winner(1)
        self.assertFalse(result)

    def test_QuoridorGame_pawn_position(self):
        """
        Tests QuoridorGame pawn_position.
        """
        q = QuoridorGame()
        result = q.pawn_position(1)
        self.assertEqual(result, (4,0))

    def test_QuoridorGame_valid_moves_42_no_fences_no_enemy(self):
        """
        Tests QuoridorGame valid_moves, P1 pawn on (4, 2), no fences blocking, no enemy adjacent.
        """
        q = QuoridorGame()
        q.amend_spaces_dict((4, 0), "  ")
        q.amend_spaces_dict((4, 2), "P1")
        q.amend_board()
        p1_position = q.pawn_position(1)
        result = q.valid_moves(p1_position)
        self.assertEqual(result, [(3, 2), (4, 1), (4, 3), (5, 2)])

    def test_QuoridorGame_valid_moves_42_up_fence_no_enemy(self):
        """
        Tests QuoridorGame valid_moves, P1 pawn on (4, 2), up fence blocking, no enemy adjacent.
        """
        q = QuoridorGame()
        q.amend_spaces_dict((4, 0), "  ")
        q.amend_spaces_dict((4, 2), "P1")
        q.amend_horiz_edges_dict((4,2), "__")
        q.amend_board()
        p1_position = q.pawn_position(1)
        result = q.valid_moves(p1_position)
        self.assertEqual(result, [(3, 2), (4, 3), (5, 2)])

    def test_QuoridorGame_valid_moves_42_bottom_fence_no_enemy(self):
        """
        Tests QuoridorGame valid_moves, P1 pawn on (4, 2), bottom fence blocking, no enemy adjacent.
        """
        q = QuoridorGame()
        q.amend_spaces_dict((4, 0), "  ")
        q.amend_spaces_dict((4, 2), "P1")
        q.amend_horiz_edges_dict((4,3), "__")
        q.amend_board()
        p1_position = q.pawn_position(1)
        result = q.valid_moves(p1_position)
        self.assertEqual(result, [(3, 2), (4, 1), (5, 2)])

    def test_QuoridorGame_valid_moves_42_left_fence_no_enemy(self):
        """
        Tests QuoridorGame valid_moves, P1 pawn on (4, 2), left fence blocking, no enemy adjacent.
        """
        q = QuoridorGame()
        q.amend_spaces_dict((4, 0), "  ")
        q.amend_spaces_dict((4, 2), "P1")
        q.amend_vert_edges_dict((4,2), "| ")
        q.amend_board()
        p1_position = q.pawn_position(1)
        result = q.valid_moves(p1_position)
        self.assertEqual(result, [(4, 1), (4, 3), (5, 2)])

    def test_QuoridorGame_valid_moves_42_right_fence_no_enemy(self):
        """
        Tests QuoridorGame valid_moves, P1 pawn on (4, 2), right fence blocking, no enemy adjacent.
        """
        q = QuoridorGame()
        q.amend_spaces_dict((4, 0), "  ")
        q.amend_spaces_dict((4, 2), "P1")
        q.amend_vert_edges_dict((5,2), "| ")
        q.amend_board()
        p1_position = q.pawn_position(1)
        result = q.valid_moves(p1_position)
        self.assertEqual(result, [(3, 2), (4, 1), (4, 3)])

    def test_QuoridorGame_valid_moves_42_no_fences_enemy_up_jump_allowed(self):
        """
        Tests QuoridorGame valid_moves, P1 pawn on (4, 2), no fences blocking, enemy up, jump allowed.
        """
        q = QuoridorGame()
        q.amend_spaces_dict((4, 0), "  ")
        q.amend_spaces_dict((4, 2), "P1")
        q.amend_spaces_dict((4, 8), "  ")
        q.amend_spaces_dict((4,1), "P2")
        q.amend_board()
        p1_position = q.pawn_position(1)
        result = q.valid_moves(p1_position)
        self.assertEqual(result, [(3, 2), (4, 0), (4, 3), (5, 2)])

    def test_QuoridorGame_valid_moves_42_no_fences_enemy_up_jump_blocked(self):
        """
        Tests QuoridorGame valid_moves, P1 pawn on (4, 2), no fences blocking, enemy down, jump blocked
        (both diag allowed).
        """
        q = QuoridorGame()
        q.amend_spaces_dict((4, 0), "  ")
        q.amend_spaces_dict((4, 2), "P1")
        q.amend_spaces_dict((4, 8), "  ")
        q.amend_spaces_dict((4,1), "P2")
        q.amend_horiz_edges_dict((4,1), "__")
        q.amend_board()
        p1_position = q.pawn_position(1)
        result = q.valid_moves(p1_position)
        self.assertEqual(result, [(3, 1), (3, 2), (4, 3), (5, 1), (5, 2)])

    def test_QuoridorGame_valid_moves_42_no_fences_enemy_up_jump_blocked_diag_up_left_blocked(self):
        """
        Tests QuoridorGame valid_moves, P1 pawn on (4, 2), no fences blocking, enemy down, jump blocked
        (diag up left blocked).
        """
        q = QuoridorGame()
        q.amend_spaces_dict((4, 0), "  ")
        q.amend_spaces_dict((4, 2), "P1")
        q.amend_spaces_dict((4, 8), "  ")
        q.amend_spaces_dict((4,1), "P2")
        q.amend_horiz_edges_dict((4,1), "__")
        q.amend_vert_edges_dict((4, 1), "| ")
        q.amend_board()
        p1_position = q.pawn_position(1)
        result = q.valid_moves(p1_position)
        self.assertEqual(result, [(3, 2), (4, 3), (5, 1), (5, 2)])

    def test_QuoridorGame_valid_moves_42_no_fences_enemy_up_jump_blocked_diag_up_right_blocked(self):
        """
        Tests QuoridorGame valid_moves, P1 pawn on (4, 2), no fences blocking, enemy down, jump blocked
        (diag up right blocked).
        """
        q = QuoridorGame()
        q.amend_spaces_dict((4, 0), "  ")
        q.amend_spaces_dict((4, 2), "P1")
        q.amend_spaces_dict((4, 8), "  ")
        q.amend_spaces_dict((4,1), "P2")
        q.amend_horiz_edges_dict((4,1), "__")
        q.amend_vert_edges_dict((5,1), "| ")
        q.amend_board()
        p1_position = q.pawn_position(1)
        result = q.valid_moves(p1_position)
        self.assertEqual(result, [(3, 1), (3, 2), (4, 3), (5, 2)])

    def test_QuoridorGame_valid_moves_42_no_fences_enemy_up_jump_blocked_both_diag_blocked(self):
        """
        Tests QuoridorGame valid_moves, P1 pawn on (4, 2), no fences blocking, enemy down, jump blocked
        (both diag blocked).
        """
        q = QuoridorGame()
        q.amend_spaces_dict((4, 0), "  ")
        q.amend_spaces_dict((4, 2), "P1")
        q.amend_spaces_dict((4, 8), "  ")
        q.amend_spaces_dict((4,1), "P2")
        q.amend_horiz_edges_dict((4,1), "__")
        q.amend_vert_edges_dict((4, 1), "| ")
        q.amend_vert_edges_dict((5,1), "| ")
        q.amend_board()
        p1_position = q.pawn_position(1)
        result = q.valid_moves(p1_position)
        self.assertEqual(result, [(3, 2), (4, 3), (5, 2)])

    def test_QuoridorGame_move_pawn_game_over(self):
        """
        Tests QuoridorGame move_pawn, game over.
        """
        q = QuoridorGame()
        q.set_game_won(True)
        result = q.move_pawn(1, (4, 1))
        self.assertFalse(result)

    def test_QuoridorGame_move_pawn_not_players_turn(self):
        """
        Tests QuoridorGame move_pawn, not player's turn.
        """
        q = QuoridorGame()
        result = q.move_pawn(2, (4, 1))
        self.assertFalse(result)

    def test_QuoridorGame_move_pawn_move_not_valid(self):
        """
        Tests QuoridorGame move_pawn, move not valid.
        """
        q = QuoridorGame()
        result = q.move_pawn(1, (8, 8))
        self.assertFalse(result)

    def test_QuoridorGame_move_pawn_move_valid(self):
        """
        Tests QuoridorGame move_pawn, move valid.
        """
        q = QuoridorGame()
        result = q.move_pawn(1, (4, 1))
        self.assertTrue(result)





if __name__ == '__main__':      # #runs the unit tests
    unittest.main()