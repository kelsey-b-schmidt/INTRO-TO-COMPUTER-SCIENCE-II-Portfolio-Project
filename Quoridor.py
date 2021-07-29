# Author: Kelsey Schmidt
# Date: 7-28-21
# Description:  # Creates a class named QuoridorGame for playing a board game called Quoridor.
                # This class plays the two-player version of the game.


class QuoridorGame:
    """
    Creates a game of Quoridor, to be played by two players.
    The board is formed by a 9x9 grid, upon which the two players will each have a pawn,
    and each player's pawn will move on the cells. Each player will have 10 fences.
    The fences can be placed on the edges of the cells, to obstruct the other player's pawn's movement.

    The board spaces are numbered 0-8 from left to right, and top to bottom.
    The four edges are labeled as fences, and the rows of the cells where the pawns
    are positioned at the start of the game (rows 0 and 8) are called base lines.

    The pawn position (k,y) is defined by the coordinate of the top left corner of the cell
    that the pawn is on. k is the number from the vertical line
    and y is the number from the horizontal line, making the top left corner of the cell.
    The board positions start with (0,0) and end at (8,8).
    At the beginning of the game, player 1 places pawn 1 (P1) on the top center of the board, (4,0),
    and player 2 places pawn 2 (P2) on the bottom center of the board, (4,8).

    When a player tries to place a fence on the board, the position of the fence is defined
    by a letter and coordinates; “v” for vertical fences, and “h” for horizontal fences,
    and a tuple of the coordinates. So, for ekample, “h”,(6,5) would be a horizontal fence
    starting at the (6,5) coordinate, and drawn one space to the right, whereas  “v”,(6,5)
    would be a vertical fence starting at the (6,5) coordinate, and drawn one space down.
    Fences only block one square, and cannot be moved once placed, nor can they be re-used.
    On each turn, players can move one space or place a fence.
    Fences cannot be arranged in such a way that makes it impossible for the other player to win,
    such as blocking a player in, or blocking the target side of the board entirely.
    (This is the fair play rule)

    A valid move for a player to make would be moving one space horizontally or vertically,
    unless blocked by a fence, with no diagonal movement allowed EkCEPT for a special condition.
    If facing the other player's piece directly, you are allowed to jump over the other piece,
    assuming no fence is behind the other player's piece that would stop that movement.
    It is in this case ONLY, when one could otherwise jump over an opponent's piece, but is blocked
    by a fence directly behind that piece, that the player can move one space *diagonally* to either
    of the spaces to the side of the opponent's piece, in lieu of going over.
    In this same scenario, if there is a fence to the *side* of the opponent's piece,
    in the intended move direction, that move is blocked by the fence, and cannot be completed.

    Player 1 will start the game. Each player takes turns playing.
    On a player’s turn they will make one move.
    They can either move the pawn (move_pawn) or place a fence (place_fence).
    The first player whose pawn reaches any of the cells of the opposite player's base line wins the game.
    No turn can be played after a player has won.

    This class contains methods:
        init
            - initializes the board with the outer four edges fenced in, and pawns (P1 and P2) placed in the correct positions.
            - All data members are private:
                board, coords_dict, spaces_dict, horiz_edges_dict, vert_edges_dict,
                game_won, winner, player_1_turn, player_2_turn
        get and set methods for all data members**, named in the usual fashion (e.g. get_data_member_name, set_data_member_name).
            (**there is not a set method for coords_dict, as the coordinates for the board remain unchanged.)
        board_generator
            - creates a new game board with the current content of the spaces and horiz/vert edges lists.
                Returns the new board configuration (a list of lists), which can then be passed to the set_board method.



        move_pawn
            - takes the following two parameters in order:
                an integer that represents which player (1 or 2) is making the move,
                and a tuple with the coordinates of where the pawn is going to be moved to.
                    (ek. move_pawn(2, (4,7))
            - if the game has been already won, returns False
            - if the move is forbidden by the fair play rule or blocked by a fence, returns False
            - if the move was successful or if the move makes the player win, returns True
        place_fence
            - takes the following parameters in order:
                an integer that represents which player (1 or 2) is making the move,
                a letter indicating whether it is a vertical (v) or horizontal (h) fence,
                and a tuple of integers that represents the position on which the fence is to be placed.
            - if the game has been already won, returns False
            - if player has no fences left, returns False
            - if the intended fence position is out of the boundaries of the board, returns False
            - if there is already a fence at the intended position, returns False
            - if the intended position breaks the "fair play rule", returns the string "breaks the fair play rule"
            - if the fence can be placed successfully, returns True
        is_winner
            - takes a single integer representing the player number (1 or 2) as a parameter,
            - returns True if that player has won and False if that player has not won.
        print_board
            - takes no parameters
            - prints the board in a pretty manner.
    """

    def __init__(self):
        """
        Initializes the board with the outer four edges fenced in, and pawns (P1 and P2) placed in the correct positions.
        All data members are private:
            board, coords_dict, spaces_dict, horiz_edges_dict, vert_edges_dict,
            game_won, winner, player_1_turn, player_2_turn
        """

        # all of these empty lists/dictionaries will get filled within the init function body

        self._board = []    # creates an empty list to hold the game board

        self._coords_dict = dict()  # creates an empty dictionary to hold the coordinates (". ", for visual clarity)
                                    # keys of the coords_dict are a tuple of the position

        self._horiz_edges_dict = dict() # creates an empty dictionary to hold the horiz edges
                                        # keys of the horiz_edges_dict are a tuple of the position
                                        # ("  " until filled with a fence, which looks like "--")

        self._vert_edges_dict = dict() # creates an empty dictionary to hold the
                                        # keys of the vert_edges_dict are a tuple of the position
                                        # ("  " until filled with a fence, which looks like "| ")

        self._spaces_dict = dict()  # creates an empty dictionary to hold the spaces ("  " unless filled with a pawn)
                                    # keys of the spaces_dict are a tuple of the position

        self._game_won = False      # the game has not been won yet

        self._winner = None         # there is no winner yet

        self._player_1_turn = True  # the game starts on player 1's turn

        self._player_2_turn = False # the game starts on player 1's turn

        for i in range(0, 10):
            for j in range(0, 10):
                self._coords_dict[(j, i)] = ". "  # fills the coords_dict

        for i in range(0, 10):
            for j in range(0, 9):
                if i == 0 or i ==9 :
                    self._horiz_edges_dict[(j, i)] = "--"
                else:
                    self._horiz_edges_dict[(j, i)] = "  "   # fill the horiz_edges_dict
                                                            # (outlines the outer edges with fences)
        for i in range(0, 9):
            for j in range(0, 10):
                if j == 0 or j == 9:
                    self._vert_edges_dict[(j, i)] = "| "
                else:
                    self._vert_edges_dict[(j, i)] = "  "    # fill the vert_edges_dict
                                                            #(outlines the outer edges with fences)

        for i in range(0, 9):
            for j in range(0, 9):
                self._spaces_dict[(j, i)] = "  "    # fill the spaces_dict with un-occupied spaces
        self._spaces_dict[(4, 0)] = "P1"  # fill in player 1's default position
        self._spaces_dict[(4, 8)] = "P2"  # fill in player 2's default position

        board = self.board_generator()    # calls the board_generator function to generate a new game board.
                            # fills up the game board (list of lists) with the edges lined and 2 pawns in starting position,
                            # since that is the current content of the spaces and horiz/vert edges lists.
        self.set_board(board)       # overwrites the current board with the new board info

        # game is ready to start!

    def get_board(self):
        """
        Returns the board list.
        """
        return self._board

    def set_board(self, board):
        """
        Takes a parameter of a new board (list of lists) (see board generator method)
        Overwrites the current board with a new configuration.
        """
        self._board = board

    def get_coords_dict(self):
        """
        Returns the coords_dict.
        """
        return self._coords_dict

    # no set method for coords_dict, as the coordinates remain unchanged through gameplay

    def get_horiz_edges_dict(self):
        """
        Returns the horiz_edges_dict.
        """
        return self._horiz_edges_dict

    def set_horiz_edges_dict(self, horiz_edges_dict):
        """
        Takes a parameter of a new horiz_edges_dict (with updates based on successful placement of a horiz fence)
        Overwrites the current horiz_edges_dict with the new configuration.
        """
        self._horiz_edges_dict = horiz_edges_dict

    def get_vert_edges_dict(self):
        """
        Returns the vert_edges_dict.
        """
        return self._vert_edges_dict

    def set_vert_edges_dict(self, vert_edges_dict):
        """
        Takes a parameter of a new vert_edges_dict (with updates based on successful placement of a vert fence)
        Overwrites the current vert_edges_dict with the new configuration.
        """
        self._vert_edges_dict = vert_edges_dict

    def get_spaces_dict(self):
        """
        Returns the spaces_dict.
        """
        return self._spaces_dict

    def set_spaces_dict(self, spaces_dict):
        """
        Takes a parameter of a new spaces_dict (with updates based on successful movement of a pawn)
        Overwrites the current spaces_dict with the new configuration.
        """
        self._vert_edges_dict = vert_edges_dict

    def get_game_won(self):
        """
        Returns the current game won state (True or False)
        """
        return self._game_won

    def set_game_won(self, boolean):
        """
        Sets the game won state (True or False)
        """
        self._game_won = boolean

    def get_winner(self):
        """
        Returns the current winner of the game (None, p1, p2)
        """
        return self._winner

    def set_winner(self, winner):
        """
        Sets the winner of the game (None, p1, p2)
        """
        self._winner = winner

    def get_player_1_turn(self):
        """
        Returns whether or not it is player 1's turn (True or False)
        """
        return self._player_1_turn

    def set_player_1_turn(self, boolean):
        """
        Sets player 1 turn to True/False.
        """
        self._player_1_turn = boolean

    def get_player_2_turn(self):
        """
        Returns whether or not it is player 2's turn (True or False)
        """
        return self._player_2_turn

    def set_player_2_turn(self, boolean):
        """
        Sets player 2 turn to True/False.
        """
        self._player_2_turn = boolean

    def board_generator(self):
        """
        Creates a new game board with the current content of the spaces and horiz/vert edges lists.
        Returns the new board configuration (a list of lists), which can then be passed to the set_board method.
        """
        coords_dict = self.get_coords_dict()    # get the current coords_dict
        horiz_edges_dict = self.get_horiz_edges_dict()    # get the current horiz_edges_dict
        vert_edges_dict = self.get_vert_edges_dict()    # get the current vert_edges_dict
        spaces_dict = self.get_spaces_dict()    # get the current spaces_dict
        board = []      # creates and empty list to hold the new board configuration
        for k in range(0, 10):  # and then fills it back up again
            horiz_row = []
            vert_row = []
            for i in range(k, k + 1):
                for j in range(0, 10):
                    if j != 9:
                        horiz_row.append(coords_dict[(j, i)])
                        horiz_row.append(horiz_edges_dict[(j, i)])
                    else:
                        horiz_row.append(coords_dict[(j, i)])
            board.append(horiz_row)
            if k == 9:
                break

            for i in range(k, k + 1):
                for j in range(0, 10):
                    if j != 9:
                        vert_row.append(vert_edges_dict[(j, i)])
                        vert_row.append(spaces_dict[(j, i)])
                    else:
                        vert_row.append(vert_edges_dict[(j, i)])
            board.append(vert_row)
        return board    # returns a new board configuration (can be passed to set_board method)





    def print_board(self):
        """
        Takes no parameters
        Prints the board in a pretty manner.
        """
        for line in self._board:
            print(*line[:])



def main():
    """
    A main function to run the program as a script or a module.
    """
    q = QuoridorGame()
    q.print_board()
    pass

if __name__ == '__main__':  # if running as a script, runs the main function
  main()