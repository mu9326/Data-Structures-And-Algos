class Symbol:
    def __init__(self, symbol: str):
        self.symbol = symbol


class Grid:
    _instance = None

    def __init__(self, n, m):
        if Grid._instance is not None:
            raise Exception("Grid has already been initialized!")
        else:
            Grid._instance = self
            self.n = n
            self.m = m
            self.count = m * n
            self.grid = [["" for _ in range(n)] for _ in range(m)]

    def get_instance():
        if Grid._instance is None:
            Grid()
        return Grid._instance

    def display_grid(self):
        return self.grid
