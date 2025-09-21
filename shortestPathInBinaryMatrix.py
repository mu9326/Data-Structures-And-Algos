from typing import List
from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        # If start or end is blocked
        if grid[0][0] == 1 or grid[rows - 1][cols - 1] == 1:
            return -1

        queue = deque([0, 0])
        visited = set()
        shortest = 0

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                r = node[0]
                c = node[1]

                if r == rows - 1 and c == cols - 1:
                    return shortest + 1
                for dr, dc in ([0, 1], [1, 1], [0, 1]):
                    nr, nc = r + dr, c + dc

                    if grid[nr][nc] == 0 and [nr, nc] not in visited:
                        queue.append([nr, nc])
                        visited.add([nr, nc])
            shortest += 1

        return -1
