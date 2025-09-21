from abc import ABC, abstractmethod
from enum import Enum


class GameStatus(Enum):
    IN_PROGRESS = 1
    WINNER_X = 2
    WINNER_O = 3
    DRAW = 4


class GameState(ABC):
    @abstractmethod
    def handleMove(self, game, player, row, col):
        pass


class InProgressState(GameState):
    def handleMove(self, game, player, row, col):
        game.board.makeMove(row, col, player.getSymbol())
        if game.checkWinner(player):
            game.setState(WinnerState(player))
        elif game.board.isFull():
            game.setState(DrawState())
        else:
            game.switchPlayer()


class WinnerState(GameState):
    def __init__(self, winner):
        self.winner = winner

    def handleMove(self, game, player, row, col):
        raise Exception("Game over! Player {} won".format(self.winner.getName()))


class DrawState(GameState):
    def handleMove(self, game, player, row, col):
        raise Exception("Game over! It's a draw")


class GameObserver(ABC):
    @abstractmethod
    def update(self, game):
        pass


class GameSubject:
    def __init__(self):
        self.observers = []

    def addObserver(self, observer):
        self.observers.append(observer)

    def removeObserver(self, observer):
        self.observers.remove(observer)

    def notifyObservers(self, game):
        for observer in self.observers:
            observer.update(game)


class Scoreboard(GameObserver):
    def __init__(self):
        self.scores = {}

    def update(self, game):
        winner = game.winner
        if winner:
            self.scores[winner.getName()] = self.scores.get(winner.getName(), 0) + 1

    def printScores(self):
        for player, score in self.scores.items():
            print(player, ":", score)
