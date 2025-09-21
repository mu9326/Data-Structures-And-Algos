from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        m, n = len(heights), len(heights[0])
        pacific_reachable = set()
        atlantic_reachable = set()

        def dfs(r, c, visited):
            visited.add((r, c))
            for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < m
                    and 0 <= nc < n
                    and (nr, nc) not in visited
                    and heights[nr][nc] >= heights[r][c]
                ):
                    dfs(nr, nc, visited)

        # DFS from Pacific Ocean (top and left edges)
        for i in range(m):
            dfs(i, 0, pacific_reachable)  # left edge
        for j in range(n):
            dfs(0, j, pacific_reachable)  # top edge

        # If you also want the full solution:
        # DFS from Atlantic Ocean (bottom and right edges)
        for i in range(m):
            dfs(i, n - 1, atlantic_reachable)  # right edge
        for j in range(n):
            dfs(m - 1, j, atlantic_reachable)  # bottom edge

        # Intersection of Pacific and Atlantic reachable cells
        result = list(pacific_reachable & atlantic_reachable)

        # Optional: Return Pacific-only set (converted to list)
        # pacific_only = list(pacific_reachable)
        return result  # or return result if you want both oceans
