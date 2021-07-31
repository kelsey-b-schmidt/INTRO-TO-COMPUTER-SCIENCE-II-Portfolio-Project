# Author: Kelsey Schmidt
# Date: 7-28-21
# Description:  # Creates a class FairPlayBroken that inherits from exception.
                # Creates a class named QuoridorGame for playing a board game called Quoridor.
                # This class plays the two-player version of the game.

class FairPlayBroken(Exception):
    """Raised if placing a fence breaks the fair play rule"""
    pass

class QuoridorGame:

    """
    Creates a game of Quoridor, to be played by two players.
    The board is formed by a 9x9 grid, upon which the two players will each have a pawn,
    and each player's pawn will move on the cells. Each player will have 10 fences.
    The fences can be placed on the edges of the cells, to obstruct the other player's pawn's movement.

    The board spaces are numbered 0-8 from left to right, and top to bottom.
    The board positions start with (0,0) and end at (8,8).
    The four edges are labeled as fences, and the rows of the cells where the pawns
    are positioned at the start of the game (rows 0 and 8) are called base lines.

    The pawn position (x,y) is defined by the coordinate of the top left corner of the cell
    that the pawn is on. x is the number from the vertical line
    and y is the number from the horizontal line, making the top left corner of the cell.
    At the beginning of the game, player 1 places pawn 1 (P1) on the top center of the board, (4,0),
    and player 2 places pawn 2 (P2) on the bottom center of the board, (4,8).

    When a player tries to place a fence on the board, the position of the fence is defined
    by a letter and coordinates; “v” for vertical fences, and “h” for horizontal fences,
    and a tuple of the coordinates. So, for example, “h”,(6,5) would be a horizontal fence
    starting at the (6,5) coordinate, and drawn one space to the right, whereas  “v”,(6,5)
    would be a vertical fence starting at the (6,5) coordinate, and drawn one space down.
    Fences only block one square, and cannot be moved once placed, nor can they be re-used.
    On each turn, players can move one space or place a fence.
    Fences cannot be arranged in such a way that makes it impossible for the other player to win,
    such as blocking a player in, or blocking the target side of the board entirely.
    (This is the fair play rule)

    A valid move for a player to make would be moving one space horizontally or vertically,
    unless blocked by a fence, with no diagonal movement allowed EXCEPT for a special condition.
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
            - initializes the board with the outer four edges fenced in,
                and pawns (P1 and P2) placed in the correct positions.
            - All data members are private:
                board, coords_dict, spaces_dict, horiz_edges_dict, vert_edges_dict,
                game_won, winner, player_turn, player_1_fences, player_2_fences
        get and set methods for all data members**, (e.g. get_data_member_name, set_data_member_name).
            - get and set private data members (overrides current content)
        amend methods for board, spaces_dict, horiz_edges_dict, vert_edges_dict, player_fences **
            (e.g amend_data_member_name)
            - make changes to the dictionaries/lists, and passes result to the appropriate set method.

                            **there are neither set nor amend methods for coords_dict,
                            as the coordinates for the board remain unchanged once initialized.**

        pawn_position
            - takes a player (1 or 2).
            - returns a tuple of the current position of the player's pawn.
        valid_moves
            - takes a tuple of a pawn's current position.
            - returns a list of valid moves (places the pawn can legally go) in any direction.
            - uses results from helper methods: valid_moves_up, valid_moves_down, valid_moves_left, valid_moves_right.
        valid_moves_up
            - takes a tuple of a pawn's current position.
            - returns a list of valid moves (places the pawn can legally go) in the upwards direction.
        valid_moves_down
            - takes a tuple of a pawn's current position.
            - returns a list of valid moves (places the pawn can legally go) in the downwards direction.
        valid_moves_left
            - takes a tuple of a pawn's current position.
            - returns a list of valid moves (places the pawn can legally go) in the leftwards direction.
        valid_moves_right
            - takes a tuple of a pawn's current position.
            - returns a list of valid moves (places the pawn can legally go) in the rightwards direction.
        move_pawn
            - Takes the following two parameters in order:
                an integer that represents which player (1 or 2) is making the move,
                and a tuple with the coordinates of the new position where the pawn is going to be moved to.
                    (ex. move_pawn(2, (4,7))
            - if the game has been already won, returns False.
            - if it is not the player's turn, returns False.
            - if the move is not valid returns False.
            - if the move is is valid, makes the move, updates the game board, updates whose turn it is,
                triggers a win if necessary, and returns True.
        fair_play
            - Takes a player (1 or 2)
            - determines if the game is win-able from the player pawn's position.
            - win-able means there are no fences blocking the player from their winning row entirely,
                either by surrounding the player (with or without touching the sides of the board)
                or creating a solid line from any of the edges that entirely blocks the player's winning row.
            - returns True if the player can win the game, and raises FairPlayBroken if not.
        valid_fences_horiz
            - determines the valid playable horizontal fence positions left on the board.
            - returns a list of valid horizontal fence positions.
        valid_fences_vert
            - determines the valid playable vertical fence positions left on the board.
            - returns a list of valid vertical fence positions.




        place_fence
            - takes the following parameters in order:
                an integer that represents which player (1 or 2) is making the move,
                a letter indicating whether it is a vertical ("v") or horizontal ("h") fence,
                and a tuple of integers that represents the position on which the fence is to be placed.
            - if the game has been already won, returns False
            - if it is not the player's turn, returns False.
            - if player has no fences left, returns False
            - if the fence placement is not valid, returns False
            - if the intended position breaks the "fair play rule", returns the string "breaks the fair play rule"
            - if the fence position is valid, makes the move, updates the game board, updates whose turn it is,
                and returns True.
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

        self._coords_dict = dict()  # creates an empty dictionary to hold the coordinates
                                    # (". ", for visual clarity)
                                    # keys of the coords_dict are a tuple of the position

        self._horiz_edges_dict = dict() # creates an empty dictionary to hold the horiz edges
                                        # ("  " until filled with a horizontal fence, which looks like "__")
                                        # keys of the horiz_edges_dict are a tuple of the position

        self._vert_edges_dict = dict()  # creates an empty dictionary to hold the vert edges
                                        # ("  " until filled with a vertical fence, which looks like "| ")
                                        # keys of the vert_edges_dict are a tuple of the position

        self._spaces_dict = dict()  # creates an empty dictionary to hold the spaces
                                    # ("  " unless filled with a pawn, "P1 " or "P2 ")
                                    # keys of the spaces_dict are a tuple of the position

        self._game_won = False      # game_won starts as False (can be True or False)

        self._winner = None         # game starts with no winner (can be None, 1, or 2)

        self._player_turn = 1  # the game starts on player 1's turn (can be 1 or 2)

        self._player_1_fences = 10  # each player starts with 10 fences

        self._player_2_fences = 10  # each player starts with 10 fences

        for i in range(0, 10):                      # fill the coords_dict
            for j in range(0, 10):                  # since this only happens once and is within the init,
                self._coords_dict[(j, i)] = ". "    # I did not make a separate amend/set method

        for i in range(0, 10):                              # fill the horiz_edges_dict with amend method
            for j in range(0, 9):                           # (outlines the outer edges with fences)
                if i == 0 or i ==9 :
                    self.amend_horiz_edges_dict((j, i), "__")
                else:
                    self.amend_horiz_edges_dict((j, i), "  ")

        for i in range(0, 9):                               # fill the vert_edges_dict with amend method
            for j in range(0, 10):                          #(outlines the outer edges with fences)
                if j == 0 or j == 9:
                    self.amend_vert_edges_dict((j, i), "| ")
                else:
                    self.amend_vert_edges_dict((j, i), "  ")

        for i in range(0, 9):
            for j in range(0, 9):
                self.amend_spaces_dict((j, i), "  ") # fill the spaces_dict with un-occupied spaces with amend method

        self.amend_spaces_dict((4,0), "P1")         # fill in player 1's default position with amend method
        self.amend_spaces_dict((4,8), "P2")         # fill in player 2's default position with amend method

        board = self.amend_board()    # calls the amend_board function to generate a new game board with current lists

        # game is ready to start!

    # get and set methods

    def get_board(self):
        """
        Returns the board list.
        """
        return self._board

    def set_board(self, board):
        """
        Takes a parameter of a new board (list of lists) (see amend_board method)
        Overwrites the current board with a new configuration.
        """
        self._board = board

    def get_coords_dict(self):
        """
        Returns the coords_dict.
        """
        return self._coords_dict

        # no set method or amend method for coords_dict, as the coordinates remain unchanged through gameplay

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
        self._spaces_dict = spaces_dict

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
        Returns the current winner of the game (None, 1, 2)
        """
        return self._winner

    def set_winner(self, player):
        """
        Sets the winner of the game (None, 1, 2)
        """
        self._winner = player

    def get_player_turn(self):
        """
        Returns whose turn it is currently (1 or 2)
        """
        return self._player_turn

    def set_player_turn(self, player):
        """
        Sets player turn to selected player (1 or 2)
        """
        self._player_turn = player

    def get_player_1_fences(self):
        """
        Returns how many fences player 1 has left.
        """
        return self._player_1_fences

    def get_player_2_fences(self):
        """
        Returns how many fences player 2 has left.
        """
        return self._player_2_fences

    def set_player_1_fences(self, integer):
        """
        Sets player_1_fences to a new integer.
        """
        self._player_1_fences = integer

    def set_player_2_fences(self, integer):
        """
        Sets player_2_fences to a new integer.
        """
        self._player_2_fences = integer

    # amend methods

    def amend_board(self):
        """
        Creates a new game board with the current content of the spaces and horiz/vert edges lists.
        Passes result to the set_board_dict method.
        """
        coords_dict = self.get_coords_dict()    # get the coords_dict
        horiz_edges_dict = self.get_horiz_edges_dict()    # get the current horiz_edges_dict
        vert_edges_dict = self.get_vert_edges_dict()    # get the current vert_edges_dict
        spaces_dict = self.get_spaces_dict()    # get the current spaces_dict
        board = []      # creates and empty list to hold the new board configuration
        for k in range(0, 10):  # and then fills it up with the current element lists
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

        self.set_board(board)    # sets the board with the set method

    def amend_horiz_edges_dict(self, key, value):
        """
        Amends the horiz_edges_dict selected key to the new value.
        Passes result to the set_horiz_edges_dict method.
        """
        horiz_edges_dict = self.get_horiz_edges_dict()
        horiz_edges_dict[key] = value
        self.set_horiz_edges_dict(horiz_edges_dict) # sets the dictionary using the set method

    def amend_vert_edges_dict(self, key, value):
        """
        Amends the vert_edges_dict selected key to the new value.
        Passes result to the set_vert_edges_dict method.
        """
        vert_edges_dict = self.get_vert_edges_dict()
        vert_edges_dict[key] = value
        self.set_vert_edges_dict(vert_edges_dict) # sets the dictionary using the set method

    def amend_spaces_dict(self, key, value):
        """
        Amends the spaces_dict selected key to the new value.
        Passes result to the set_spaces_dict method.
        """
        spaces_dict = self.get_spaces_dict()
        spaces_dict[key] = value
        self.set_spaces_dict(spaces_dict) # sets the dictionary using the set method

    def amend_player_fences(self, player, integer):
        """
        Amends the selected player's fence stock by the integer.
        Passes result to the set_player_fence method for the chosen player.
        """
        fences = None
        if player == 1:                         # if the player is 1
            fences = self.get_player_1_fences()
            fences += integer
            self.set_player_1_fences(fences)
        elif player ==2:                        # if the player is 2
            fences = self.get_player_2_fences()
            fences += integer
            self.set_player_2_fences(fences)




    # other methods

    def pawn_position(self, player):
        """
        Takes a player (1 or 2).
        Returns a tuple of the current position of the player's pawn.
        """
        spaces_dict = self.get_spaces_dict()
        for key in spaces_dict:
            if str(player) not in spaces_dict[key]:
                continue
            else:
                return key

    def valid_moves(self, position):
        """
        Takes a tuple of a pawn's current position.
        Returns a list of valid moves (places the pawn can legally go) in any direction.
        Uses results from helper methods: valid_moves_up, valid_moves_down, valid_moves_left, valid_moves_right.
        """
        valid_moves = []    # create an empty list to hold the valid moves

        valid_moves_up = self.valid_moves_up(position)  # run valid_moves_up
        valid_moves_down = self.valid_moves_down(position)  # run valid_moves_down
        valid_moves_left = self.valid_moves_left(position)  # run valid_moves_left
        valid_moves_right = self.valid_moves_right(position)  # run valid_moves_right
        for move in set(valid_moves_up) | set(valid_moves_down) | set(valid_moves_left) | set(valid_moves_right):
            # for each move that is in any, some, or all of the lists (gets only unique moves
            valid_moves.append(move)  # add the move
        valid_moves.sort() # sort the list for easy reading
        return valid_moves

    def valid_moves_up(self, position):
        """
        Takes a tuple of a pawn's current position.
        Returns a list of valid moves (places the pawn can legally go) in the upwards direction.
        """
        horiz_edges_dict = self.get_horiz_edges_dict()
        vert_edges_dict = self.get_vert_edges_dict()
        spaces_dict = self.get_spaces_dict()
        x = position[0]
        y = position[1]
        valid_moves = []

        if horiz_edges_dict[x, y] == "  ":  # if the top edge is open
            if spaces_dict[x, y-1] == "  ":     # if the top space is open
                valid_moves.append((x, y-1))        # top space is valid
            else:                               # if the top space is not open (has a pawn in it)
                if horiz_edges_dict[x, y-1] == "  ":    # if the edge above that is open
                    valid_moves.append((x, y-2))          # jumping over the pawn to next top space is valid
                else:                                   # if the pawn has a fence above it we can try to move diagonally
                    if vert_edges_dict[x, y-1] == "  ":     # if the edge to the left of the enemy pawn is open
                        valid_moves.append((x-1, y - 1))        # moving up diagonally to the left is valid
                    if vert_edges_dict[x+1, y-1] == "  ":     # if the edge to the right of the enemy pawn is open
                        valid_moves.append((x+1, y-1))        # moving up diagonally to the right is valid
        # if we make it all the way here and no upwards move was valid, the list will be empty
        return valid_moves  # returns the list if valid upwards moves

    def valid_moves_down(self, position):
        """
        Takes a tuple of a pawn's current position.
        Returns a list of valid moves (places the pawn can legally go) in the downwards direction.
        """
        horiz_edges_dict = self.get_horiz_edges_dict()
        vert_edges_dict = self.get_vert_edges_dict()
        spaces_dict = self.get_spaces_dict()
        x = position[0]
        y = position[1]
        valid_moves = []

        if horiz_edges_dict[x, y+1] == "  ":  # if the bottom edge is open
            if spaces_dict[x, y+1] == "  ":     # if the bottom space is open
                valid_moves.append((x, y+1))        # bottom space is valid
            else:                               # if the bottom space is not open (has a pawn in it)
                if horiz_edges_dict[x, y+2] == "  ":    # if the edge below that is open
                    valid_moves.append((x, y+2))          # jumping over the pawn to next bottom space is valid
                else:                                   # if the pawn has a fence below it we can try to move diagonally
                    if vert_edges_dict[x, y+1] == "  ":     # if the edge to the left of the enemy pawn is open
                        valid_moves.append((x-1, y+1))        # moving down diagonally to the left is valid
                    if vert_edges_dict[x+1, y+1] == "  ":     # if the edge to the right of the enemy pawn is open
                        valid_moves.append((x+1, y+1))        # moving down diagonally to the right is valid
        # if we make it all the way here and no downwards move was valid, the list will be empty
        return valid_moves  # returns the list if valid downwards moves

    def valid_moves_left(self, position):
        """
        Takes a tuple of a pawn's current position.
        Returns a list of valid moves (places the pawn can legally go) in the leftwards direction.
        """
        horiz_edges_dict = self.get_horiz_edges_dict()
        vert_edges_dict = self.get_vert_edges_dict()
        spaces_dict = self.get_spaces_dict()
        x = position[0]
        y = position[1]
        valid_moves = []

        if vert_edges_dict[x, y] == "  ":  # if the left edge is open
            if spaces_dict[x-1, y] == "  ":     # if the left space is open
                valid_moves.append((x-1, y))        # left space is valid
            else:                               # if the left space is not open (has a pawn in it)
                if vert_edges_dict[x-1, y] == "  ":    # if the edge to the left of that is open
                    valid_moves.append((x-2, y))          # jumping over the pawn to next left space is valid
                else:                          # if the pawn has a fence to the left of it we can try to move diagonally
                    if horiz_edges_dict[x-1, y+1] == "  ":     # if the edge on the bottom of the enemy pawn is open
                        valid_moves.append((x-1, y+1))        # moving left diagonally downwards is valid
                    if horiz_edges_dict[x-1, y] == "  ":     # if the edge on top of the enemy pawn is open
                        valid_moves.append((x-1, y-1))        # moving left diagonally upwards is valid
        # if we make it all the way here and no leftwards move was valid, the list will be empty
        return valid_moves  # returns the list if valid leftwards moves

    def valid_moves_right(self, position):
        """
        Takes a tuple of a pawn's current position.
        Returns a list of valid moves (places the pawn can legally go) in the rightwards direction.
        """
        horiz_edges_dict = self.get_horiz_edges_dict()
        vert_edges_dict = self.get_vert_edges_dict()
        spaces_dict = self.get_spaces_dict()
        x = position[0]
        y = position[1]
        valid_moves = []

        if vert_edges_dict[x+1, y] == "  ":  # if the right edge is open
            if spaces_dict[x+1, y] == "  ":     # if the right space is open
                valid_moves.append((x+1, y))        # right space is valid
            else:                               # if the right space is not open (has a pawn in it)
                if vert_edges_dict[x+2, y] == "  ":    # if the edge to the right of that is open
                    valid_moves.append((x+2, y))          # jumping over the pawn to next right space is valid
                else:                          # if the pawn has a fence to the right of it we can try to move diagonally
                    if horiz_edges_dict[x+1, y+1] == "  ":     # if the edge on the bottom of the enemy pawn is open
                        valid_moves.append((x+1, y+1))        # moving right diagonally downwards is valid
                    if horiz_edges_dict[x+1, y] == "  ":     # if the edge on top of the enemy pawn is open
                        valid_moves.append((x+1, y-1))        # moving right diagonally upwards is valid
        # if we make it all the way here and no rightwards move was valid, the list will be empty
        return valid_moves  # returns the list if valid rightwards moves

    def move_pawn(self, player, position):
        """
        Takes the following two parameters in order:
            an integer that represents which player (1 or 2) is making the move,
            and a tuple with the coordinates of the new position where the pawn is going to be moved to.
                (ex. move_pawn(2, (4,7))
        If the game has been already won, returns False.
        If it is not the player's turn, return False.
        If the move is not valid returns False.
        If the move is is valid, makes the move, updates the game board,
            updates whose turn it is, triggers a win if necessary, and returns True.
        """
        current_pawn_position = self.pawn_position(player)  # get the current position of the player's pawn
        valid_moves = self.valid_moves(current_pawn_position)  # get the valid moves from that space
        winning_row = None  # make the default winning row none
        if player == 1:  # if the player is 1
            winning_row = 8  # the winning row is 8 - (0, 8), (1, 8), (2, 8), etc.
        elif player == 2:  # if the player is 2
            winning_row = 0  # the winning row is 0 - (0, 0), (1, 0), (2, 0), etc.

        if self.get_game_won() == True:     # if the game has been won already
            return False                    # return False

        elif self.get_player_turn() != player:    # if it's not the selected player's turn
            return False                    # return False

        elif position not in valid_moves: # if the intended position is not a valid move
            return False                # return False

        else:
            self.amend_spaces_dict(current_pawn_position, "  ") # resets the current pawn position to blank in the spaces_dict
            if player == 1:                             # if the player is 1
                self.amend_spaces_dict(position, "P1")  # set the P1 pawn to the new position in the spaces_dict
                self.amend_board()  # amends the board with the spaces_dict positions
                if position[1] == winning_row:                    # if player 1 reached a winning position
                    self.set_game_won(True)             # set game_won to True
                    self.set_winner(1)                  # set the winner to player 1
                self.set_player_turn(2)                 # change to player 2's turn
                return True                             # return True
            if player == 2:                             # if the player is 2
                self.amend_spaces_dict(position, "P2")  # set the P2 pawn to the new position in the spaces_dict
                self.amend_board()  # amends the board with the spaces_dict positions
                if position[1] == winning_row:                    # if player 2 reached a winning position
                    self.set_game_won(True)             # set game_won to True
                    self.set_winner(2)                  # set the winner to player 2
                self.set_player_turn(1)                 # change to player 1's turn
                return True                             # return True

    def fair_play(self, player):
        """
        Takes a player (1 or 2)
        Determines if the game is win-able from the player pawn's position.
        Win-able means there are no fences blocking the player from their winning row entirely,
        either by surrounding the player (with or without touching the sides of the board)
        or creating a solid line from any of the edges that entirely blocks the player's winning row.
        Returns True if the player can win the game, and False if not.
        """
        position = self.pawn_position(player)   # get the position of the player's pawn
        winning_row = None                      # make the default winning row none
        if player == 1:                         # if the player is 1
            winning_row = 8                         # the winning row is 8 - (0, 8), (1, 8), (2, 8), etc.
        elif player ==2:                        # if the player is 2
            winning_row = 0                         # the winning row is 0 - (0, 0), (1, 0), (2, 0), etc.

        move_pool = []                          # create an empty list to hold a move pool for the pawn

        valid_moves = self.valid_moves(position)    # get the valid moves from the player's current position
        for position in valid_moves:
            move_pool.append(position)              # and add them to the move pool (we start with checking these)

        for position in move_pool:              # for each position in the move pool (we will add more within the loop)
            if position[1] != winning_row:          # if we haven't reached the winning row yet
                valid_moves = self.valid_moves(position)    # get the valid moves from that position
                for position in valid_moves:                # for each position in the valid moves
                    if position[1] != winning_row:              # if we haven't reached the winning row yet
                        if position in move_pool:                   # if the position is already in the move pool
                            continue                                    # we don't want to check it again, so continue
                        else:                                       # otherwise (position hasn't been checked yet)
                            move_pool.append(position)              # add it to the move pool (to be checked)
                    else:                                   # if we reach the winning row with the move pool
                        return True                         # the game is winnable and we return True

        raise FairPlayBroken # if we make it through checking all the board positions and cannot reach the winning row
                                # the game is not winnable, and we raise a FairPlayBroken error
                                # (handled when placing a fence)

    def valid_fences_horiz(self):
        """
        Determines the valid playable horizontal fence positions left on the board.
        Returns a list of valid horizontal fence positions.
        """
        horiz_edges_dict = self.get_horiz_edges_dict()  # get the current horiz_edges_dict
        valid_horiz_edges_left = []                  # make an empty list to hold the positions of edges that are empty

        for edge in horiz_edges_dict:                   # for each key in the dictionary
            if horiz_edges_dict[edge] == "  ":          # if the value of that key is "  " (meaning the edge is empty)
                valid_horiz_edges_left.append(edge)     # add the key (position) to the list

        return valid_horiz_edges_left                   # returns the completed list

    def valid_fences_vert(self):
        """
        Determines the valid playable vertical fence positions left on the board.
        Returns a list of valid vertical fence positions.
        """
        vert_edges_dict = self.get_vert_edges_dict()  # get the current vert_edges_dict
        valid_vert_edges_left = []                  # make an empty list to hold the positions of edges that are empty

        for edge in vert_edges_dict:                   # for each key in the dictionary
            if vert_edges_dict[edge] == "  ":          # if the value of that key is "  " (meaning the edge is empty)
                valid_vert_edges_left.append(edge)     # add the key (position) to the list

        return valid_vert_edges_left                   # returns the completed list

    def place_fence(self, player, direction, position):
        """
        Takes the following parameters in order:
            an integer that represents which player (1 or 2) is making the move,
            a letter indicating whether it is a vertical ("v") or horizontal ("h") fence,
            and a tuple of integers that represents the position on which the fence is to be placed.
        If the game has been already won, returns False
        If it is not the player's turn, returns False.
        If player has no fences left, returns False
        If the fence placement is not valid, returns False
        If the intended position breaks the "fair play rule", returns the string "breaks the fair play rule"
        If the fence position is valid, makes the move, updates the game board, updates whose turn it is,
            and returns True.
        """
        fences = None
        if player == 1:                             # if the player is 1
            fences = self.get_player_1_fences()     # get their number of fences
        elif player == 2:                           # if the player is 2
            fences = self.get_player_2_fences()     # get their number of fences

        if self.get_game_won() == True:     # if the game has been won already
            return False                    # return False

        elif self.get_player_turn() != player:    # if it's not the selected player's turn
            return False                        # return False

        elif fences == 0:     # if the player is out of fences
            return False    # return False

        valid_fence_positions = None

        if direction == "h":    # if the player wants to place a horizontal fence
            valid_fence_positions = self.valid_fences_horiz()   # get the valid horizontal fence positions
        elif direction == "v":  # if the player is trying to place a vertical fence
            valid_fence_positions = self.valid_fences_vert()    # get the valid vertical fence positions

        if position not in valid_fence_positions: # if the intended position is not a valid place to put a fence
            return False                            # return False

        try:            # we need to try to make the move and then run the fair play rule
            self.amend_player_fences(player, -1)  # lowers the player's fence count by 1
            if direction == "h":                            # if placing a horizontal fence
                self.amend_horiz_edges_dict(position, "__") # put it in the position
            elif direction == "v":                          # if placing a vertical fence
                self.amend_vert_edges_dict(position, "| ")  # put it in the position

            self.amend_board()  # amends the board with the new fence

            if player == 1:                 # if the player is 1
                self.set_player_turn(2)     # change to player 2's turn
                self.fair_play(2)           # run fair play for the other player (may raise FairPlayBroken)
            elif player == 2:               # if the player is 2
                self.set_player_turn(1)     # change to player 1's turn
                self.fair_play(1)           # run fair play for the other player (may raise FairPlayBroken)
            return True         # if no FairPlayBroken is raised, we return True, and the fence placement is done

        except FairPlayBroken:   # if the fair play rule has been broken, undo everything we did, and returns a string
            self.amend_player_fences(player, 1)  # raises the player's fence count back by 1
            if direction == "h":  # if placing a horizontal fence
                self.amend_horiz_edges_dict(position, "  ")  # takes the fence back out
            elif direction == "v":  # if placing a vertical fence
                self.amend_vert_edges_dict(position, "  ")  # takes the fence back out

            self.amend_board()  # amends the board, removing the new fence

            if player == 1:  # if the player is 1
                self.set_player_turn(1)  # change back to to player 1's turn
            elif player == 2:  # if the player is 2
                self.set_player_turn(2)  # change back to player 2's turn
            return "breaks the fair play rule"







    def is_winner(self, player):
        """
        Takes a single integer representing the player number (1 or 2) as a parameter,
        Returns True if that player has won and False if that player has not won.
        """
        winner = self.get_winner()
        if winner == player:
            return True
        else:
            return False

    def print_board(self):
        """
        Takes no parameters
        Prints the board in a pretty manner.
        """
        board = self.get_board()    # get the board
        for line in board:          # print the board out, line by line
            print(*line[:])



def main():
    """
    A main function to run the program as a script or a module.
    """
    q = QuoridorGame()
    q.move_pawn(1, (4, 1))  # moves the Player1 pawn -- valid move, returns True
    q.move_pawn(2, (4, 7))  # moves the Player2 pawn -- valid move, returns True
    q.place_fence(1, 'h', (6, 5))  # places Player1's fence -- returns True
    q.place_fence(2, 'v', (3, 3))  # places Player2's fence -- returns True
    q.is_winner(1)  # returns False because Player 1 has not won
    q.is_winner(2)  # returns False because Player 2 has not won

    print()

    q.print_board()



    pass

if __name__ == '__main__':  # if running as a script, runs the main function
  main()