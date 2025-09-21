from typing import List
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        numIslands = 0

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
                # if the cell is equal to "0" (string)
                if grid[row][col] == "0":
                    continue

                if (row, col) in visited:
                    continue
                else:
                    # BFS algorithm
                    # queue = [(0, 0)]
                    queue = deque()
                    queue.append((row, col))
                    visited.add((row, col))
                    numIslands += 1  # numIslands = 1

                    # queue = [(1, 0), (0, 2), (1, 1)]
                    # while the queue is not empty:
                    while queue:
                        print("queue: ", queue)
                        # we pop from the queue as the curr element
                        curr = queue.popleft()  # curr = (1, 0)
                        print("curr: ", curr)
                        # # mark the element as seen
                        # visited.add((curr[0], curr[1]))
                        # we explore all four directions of the curr
                        # 3 possibilities - out of bound (water), 1, 0
                        directions = get_directions(curr[0], curr[1])
                        for d in directions:
                            # d = (1, 1)
                            m = len(grid)
                            n = len(grid[0])
                            if d[0] < 0 or d[1] < 0:
                                continue
                            if d[0] >= m or d[1] >= n:
                                continue
                            elif grid[d[0]][d[1]] == "0":
                                continue
                            else:
                                if d not in visited:
                                    queue.append(d)
                                    visited.add(d)

                        # out of bounds or 0:
                        # continue
                        # 1:
                        # if the element is not already seen
                        # add this cell to the queue
        # return numIslands
        return numIslands


grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "1", "1"],
]
print(Solution().numIslands(grid))
