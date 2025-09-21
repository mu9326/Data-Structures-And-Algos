# - Requirements

# The Tic-Tac-Toe game should be played on a 3x3 grid.
# Two players take turns marking their symbols (X or O) on the grid.
# The first player to get three of their symbols in a row (horizontally, vertically, or diagonally) wins the game.
# If all the cells on the grid are filled and no player has won, the game ends in a draw.
# The game should have a user interface to display the grid and allow players to make their moves.
# The game should handle player turns and validate moves to ensure they are legal.
# The game should detect and announce the winner or a draw at the end of the game.

# 3 * 3 grid
# 2 players with one symbol each - 'X'/'O'
# Take turns placing their symbols
# Every move should be validated -
# (within the bounds of the grid, an existing symbol should not be there, it should be the player's turn)
# winning strategy - get three of their symbols in a row (h, v, d)
# draw strategy - all the cells filled and no player won
# Announce the winner at the end of the game


class Game:
    # initialize the grid
    # initialize the players alongwith their symbols
    # initialize the turnManager
    
    # initialize a spot for the player to make a move
    # make_move(symbol, spot)

    # if the player has won:
        


class Symbol:
    def __init__(self, symbol: str):
        self.symbol = symbol

    def getSymbol(self):
        return self.symbol


class TurnManager:
    def __init__(self):
        self.turn = None
        pass

    def assignTurn(self, player: Player):
        self.turn = Player
        pass

    def isTurn(self, player):
        if self.turn == player:
            return True
        return False


class Spot:
    def __init__(self, row_num, col_num):
        # initialize grid
        pass

    def is_last_winning_spot(self):
        # check ALL cells horizontal to the current spot:
            # if all of them are equal to the current symbol:
                # return True

        # check ALL cells vertical to the current spot:
            # # if all of them are equal to the current symbol:
                # return True

        # check ALL cells diagonal to the current spot:
            # if all of them are equal to the current symbol:
                # return True

        # return False
        pass


    def make_move(self, symbol):
        # (within the bounds of the grid, an existing symbol should not be there,
        # it should be the player's turn)


        pass

    def is_empty(self, symbol):
        pass

    def get_symbol(self):
        pass


class Grid:
    _instance = None

    def __init__(self, n, m):
        # rows
        # cols
        # count
        # grid
        pass

    def display_grid():
        pass


class Player:
    def __init__(self, name, symbol):
        # username
        # symbol
        pass

    def get_username(self):
        pass

    def get_symbol(self):
        pass
