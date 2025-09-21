from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
        m = len(grid)  # 3
        n = len(grid[0])  # 3
        # initialize the res with default values
        dp = [[float("inf")] * (n + 1) for _ in range(m + 1)]

        # print(dp)

        # seed the first value at the
        dp[1][1] = grid[0][0]

        # iterate over the grid
        for i in range(m + 1):
            for j in range(n + 1):
                # if there is a value at the current position:
                if dp[i][j] != float("inf"):
                    # check if the right position is within bounds:
                    if j + 1 <= n:
                        # if it is, we update the right with the min(value at right in res, value at right in grid + value at the curr position in res)
                        dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + grid[i - 1][j])
                    # check if the down position is within bounds:
                    if i + 1 <= m:
                        # if it is, we update the down position with the min(value at down in res, value at down in grid + value at the curr position in res)
                        dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + grid[i][j - 1])

        # print(dp)
        # return value at dp[m][n]
        return dp[m][n]


print(Solution().minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
