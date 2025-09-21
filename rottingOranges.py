from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # initialize freshOranges
        freshOranges = 0
        m, n = len(grid), len(grid[0])
        queue = deque()

        # iterate over the grid
        for i in range(m):
            for j in range(n):
                # if the cell value is equal to 2:
                # append rotten oranges coords to the queue
                if grid[i][j] == 2:
                    queue.append((i, j))
                # if the cell value if equal to 1:
                # increase the num of freshOranges by 1
                if grid[i][j] == 1:
                    freshOranges += 1

        if freshOranges == 0:
            return 0

        # initialize min here
        time = 0
        # start multi-source BFS
        # while the queue is not empty:
        while queue:
            flag = False
            # take a snapshot of the queue in a given minute
            for _ in range(len(queue)):
                # pop the curr element from the queue
                r, c = queue.popleft()
                # iterate over its neighbors:
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    if (
                        (0 <= (r + dr) < m)
                        and (0 <= (c + dc) < n)
                        and grid[r + dr][c + dc] == 1
                    ):
                        # update the value at the nei coords to 2
                        grid[r + dr][c + dc] = 2
                        # append the nei coords to the queue
                        queue.append((r + dr, c + dc))
                        # decrease freshOranges by 1
                        freshOranges -= 1
                        flag = True

            if flag:
                # increase min
                time += 1

        if freshOranges == 0:
            return time
        else:
            return -1


print(Solution().orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
