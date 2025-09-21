from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # initialize the minutes and freshOranges variable
        mins, freshOranges = 0, 0
        flag = False
        # initialize the queue
        queue = deque()
        # iterate over the grid and add 2-labeled cells to the queue
        for row in range(m):
            for col in range(n):
                # And count the number of freshOranges
                orange = grid[row][col]
                if orange == 2:
                    queue.append((row, col))
                elif orange == 1:
                    freshOranges += 1

        # while the queue is not empty:
        while queue:
            # for items in the queue:
            for _ in range(len(queue)):
                # queue.pop is our curr item
                r, c = queue.popleft()

                # we want to get its neighbours
                for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    # turn the cell values to 2
                    if (
                        0 <= r + dr < m
                        and 0 <= c + dc < n
                        and grid[r + dr][c + dc] == 1
                    ):
                        # change the flag to True
                        grid[r + dr][c + dc] = 2

                        flag = True
                        # add the coords of the neighbors to the queue
                        queue.append((r + dr, c + dc))
                        # decrease the num of freshOranges
                        freshOranges -= 1

            # if flag is True:
            if flag:
                # increase the minutes
                mins += 1
            flag = False

        # return mins if freshOranges count is 0, else -1
        return mins if freshOranges == 0 else -1


print(Solution().orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))

print(Solution().orangesRotting([[0, 2]]))
