from typing import List
from collections import deque


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        # initialize the queue and the visited set
        queue = deque()
        visited = set()
        m, n = len(rooms), len(rooms[0])

        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i, j))
                    visited.add((i, j))

        dist = 0

        # run BFS (while queue:)
        while queue:
            # take a snapshot of the queue - for loop over the curr length
            for _ in range(len(queue)):
                # curr = (1, 1)
                r, c = queue.popleft()
                # pop the curr
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    # iterate over the neighbors of the curr:
                    # if nei is within bounds and not equal to 1 and not equal to 0 and not visited:
                    if (
                        ((0 <= (r + dr) < m) and (0 <= (c + dc) < n))
                        and rooms[r + dr][c + dc] != 0
                        and rooms[r + dr][c + dc] != -1
                        and ((r + dr, c + dc) not in visited)
                    ):
                        rooms[r + dr][c + dc] = dist + 1
                        queue.append((r + dr, c + dc))
                        visited.add((r + dr, c + dc))

                # outside the for loop - update dist += 1
            dist += 1

        print(rooms)

    # wihout using the visited set
    def wallsAndGates2(self, rooms: List[List[int]]) -> None:
        """
        Modify rooms in-place to fill each empty room with the distance to its nearest gate.
        """
        if not rooms or not rooms[0]:
            return

        queue = deque()
        m, n = len(rooms), len(rooms[0])

        # Step 1: Add all gates to the queue
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i, j))

        dist = 0

        # Step 2: BFS from all gates
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and rooms[nr][nc] == 2147483647:
                        rooms[nr][nc] = rooms[r][c] + 1
                        queue.append((nr, nc))
            dist += 1  # This line is technically not needed with the fix above

        print(rooms)


rooms = [
    [2147483647, -1, 0, 2147483647],
    [2147483647, 2147483647, 2147483647, -1],
    [2147483647, -1, 2147483647, -1],
    [0, -1, 2147483647, 2147483647],
]
print(Solution().wallsAndGates(rooms))
