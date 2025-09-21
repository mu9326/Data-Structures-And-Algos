class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # initialize seen and set_p
        seen = set()
        set_p = set()

        m, n = len(heights), len(heights[0])  # m = 5, n = 5

        for j in range(m):
            set_p.add((0, j))
            seen.add((0, j))

        for i in range(0, n):
            set_p.add((i, 0))
            seen.add((i, 0))

        def dfs(node_pos, nei_pos):
            node_row, node_col = node_pos
            nei_row, nei_col = nei_pos
            # base case:
            # 0, 0 and # 0, 1
            if nei_row < 0 or nei_col < 0 or nei_row >= m or nei_col >= n:
                return False

            if heights[node_row][node_col] > heights[nei_row][nei_col]:
                return False

            # # If already visited, don't revisit
            # if (nei_row, nei_col) in seen:
            #     return

            # recursive case
            # mark the node as visited
            # seen ((3, 1))
            # seen.add((nei_row, nei_col))
            # for each neighbor of the node:
            # neighbors = [(4, 1)]
            for r_off, c_off in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                r, c = nei_row + r_off, nei_col + c_off
                if 0 <= r < m and 0 <= c < n:
                    # if neighbour is not in seen and the neighbour is not in the set
                    # and its value is greater than that of the the node:
                    if (
                        (r, c) not in seen
                        and (r, c) not in set_p
                        and heights[r][c] >= heights[nei_row][nei_col]
                    ):
                        seen.add((r, c))
                        set_p.add((r, c))
                    # recurse on the neighbor
                    # ((3, 1), (4, 1))
                    dfs((nei_row, nei_col), (r, c))

        i, j = 0, 0
        for r_off, c_off in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            r, c = i + r_off, j + c_off
            # call the first function
            dfs((0, 0), (r, c))

        print("set_p: ", set_p)
