from typing import List
from collections import deque


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
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
