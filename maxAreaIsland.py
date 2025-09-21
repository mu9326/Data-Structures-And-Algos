from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(r, c):
            if not (0 <= r < m and (0 <= c < n)) or grid[r][c] == 0:
                return 0

            grid[r][c] = 0
            area = 1

            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                # r, c = r + dr, c + dc
                area += dfs(r + dr, c + dc)

            return area

        # iterate over the grid
        m, n = len(grid), len(grid[0])
        maxArea = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue

                else:
                    area = 0
                    area = dfs(i, j)
                    print("area: ", area)

                    maxArea = max(area, maxArea)

        return maxArea


grid = [[1, 1, 0, 0], [1, 0, 0, 0], [0, 0, 1, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
print(Solution().maxAreaOfIsland(grid))
