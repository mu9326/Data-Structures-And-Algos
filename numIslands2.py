from typing import List


# Recursive DFS solution
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        numIslands = 0

        def dfs(row, col) -> None:
            # base case
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
                return

            # if it's equal to "0" or if it's out of range:
            if grid[row][col] == "0":
                return

            # if it has already been visted:
            if (row, col) in visited:
                return

            # recursive step
            # call dfs on all four neighbours
            # [(0, -1), (0, 1), (-1, 0), (1, 0)]
            visited.add((row, col))
            for d in get_directions(row, col):
                dfs(d[0], d[1])
            return

        def get_directions(row, col):
            directions = [
                (row, col - 1),
                (row, col + 1),
                (row - 1, col),
                (row + 1, col),
            ]
            return directions

        # iterate over each cell of the grid
        # visited = ((0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1))
        # row = 0
        for row in range(0, len(grid)):
            # col = 0
            for col in range(0, len(grid[0])):
                if grid[row][col] == "0":
                    continue

                if (row, col) in visited:
                    continue

                else:
                    # DFS
                    dfs(row, col)
                    numIslands += 1

        return numIslands


grid = [
    ["1", "1", "1", "0", "1"],
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "1", "1"],
]
print(Solution().numIslands(grid))
