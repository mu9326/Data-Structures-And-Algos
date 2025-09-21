from enum import Enum
from abc import ABC, abstractmethod
from collections import deque


class WinningStrategy(ABC):
    @abstractmethod
    def recordMove(self, row, col, marker):
        pass


class RowWinningStrategy(WinningStrategy):
    def __init__(self, size):
        self.size = size
        self.rowCounts = {}

    def recordMove(self, row, col, marker):
        self.rowCounts[row] = self.rowCounts.get(row, {})
        self.rowCounts[row][marker] = self.rowCounts[row].get(marker, 0) + 1
        if self.rowCounts[row][marker] == self.size:
            return True


class ColWinningStrategy(WinningStrategy):
    def __init__(self, size):
        self.size = size
        self.colCounts = {}

    def recordMove(self, row, col, marker):
        self.colCounts[col] = self.colCounts.get(col, {})
        self.colCounts[col][marker] = self.colCounts[col].get(marker, 0) + 1

        if self.colCounts[col][marker] == self.size:
            return True


class DiagWinningStrategy(WinningStrategy):
    def __init__(self, size):
        self.size = size
        self.diagCounts = {}

    def recordMove(self, row, col, marker):
        if row == col:
            self.diagCounts["forwards"] = self.diagCounts.get("forwards", {})
            self.diagCounts["forwards"][marker] = (
                self.diagCounts["forwards"].get(marker, 0) + 1
            )

            if self.diagCounts["forwards"][marker] == self.size:
                return True

        if row + col == self.size - 1:
            self.diagCounts["backwards"] = self.diagCounts.get("backwards", {})
            self.diagCounts["backwards"][marker] = (
                self.diagCounts["backwards"].get(marker, 0) + 1
            )

            if self.diagCounts["backwards"][marker] == self.size:
                return True

        return False


class SymbolType(Enum):
    X = "X"
    O = "O"


class Symbol(ABC):
    def __init__(self, symbol_type: SymbolType):
        self.symbol_type = symbol_type


class SymbolX(Symbol):
    def __init__(self):
        super().__init__(SymbolType.X)


class SymbolO(Symbol):
    def __init__(self):
        super().__init__(SymbolType.O)


class Board:
    def __init__(self, size):
        self.size = size
        self.board = [["" for _ in range(size)] for _ in range(size)]
        self.strategies = [
            RowWinningStrategy(size),
            ColWinningStrategy(size),
            DiagWinningStrategy(size),
        ]
        self.moveCount = 0

    def makeMove(self, row, col, symbol):
        if self.board[row][col] != "":
            raise ValueError
        else:
            marker = symbol.symbol_type
            self.board[row][col] = marker
            self.moveCount += 1
            # Delegate win detection
            for strategy in self.strategies:
                if strategy.recordMove(row, col, marker):
                    return True
            return False

    def isFull(self):
        return self.moveCount == self.size * self.size

    def __str__(self):
        lines = []
        for row in self.board:
            # Replace empty with a space for better visibility
            lines.append(" | ".join(cell if cell else " " for cell in row))
        return "\n" + "\n" + "-" * (self.size * 4 - 3) + "\n".join(lines)


class Player:
    def __init__(self, name: str, symbol: Symbol):
        self.name = name
        self.symbol = symbol

    def __repr__(self):
        return f"Player(name={self.name}, symbol={self.symbol.symbol_type.value})"

    def getSymbol(self):
        return self.symbol

    def getName(self):
        return self.name


class Game:
    def __init__(self):
        self.players = deque()
        self.initializeGame()

    def initializeGame(self):
        # initialize the board
        self.board = Board(3)

        # initialize the players with instances, not classes
        player1 = Player("Mark", SymbolX())
        player2 = Player("Kylie", SymbolO())

        # add the players to the deque
        self.players.append(player1)
        self.players.append(player2)

    def startGame(self):
        gameOver = False

        while not gameOver:
            currPlayer = self.players.popleft()

            print("Player ", currPlayer.getName(), "'s turn: ")
            row = int(input("Row: "))
            col = int(input("Col: "))

            if self.board.makeMove(row, col, currPlayer.getSymbol()):
                print("Player ", currPlayer.getName(), " has won the game!")
                gameOver = True
            elif self.board.isFull():
                print("It's a tie!")
                gameOver = True
            else:
                self.players.append(currPlayer)


def main():
    game = Game()
    game.initializeGame()
    game.startGame()


if __name__ == "__main__":
    main()
