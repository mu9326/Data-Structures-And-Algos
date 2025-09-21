from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # initialize the dp array with default values
        dp = [float("inf") for _ in range(len(cost) + 1)]

        # seed the initial values
        dp[0], dp[1] = cost[0], cost[1]

        # iterate over the array
        for i in range(len(dp)):
            # if value at i != 0
            if dp[i] != float("inf"):
                # if i + 1 < len(dp) - 1:
                if i + 1 < len(dp) - 1:
                    new_cost = cost[i + 1] + dp[i]
                    # replace dp[i+1] with new_cost only if it's lower than the current value
                    dp[i + 1] = min(dp[i + 1], new_cost)
                # do the same for dp{i+2}
                if i + 2 < len(dp) - 2:
                    new_cost = cost[i + 2] + dp[i]
                    # replace dp[i+2] with new_cost only if it's lower than the current value
                    dp[i + 2] = min(dp[i + 2], new_cost)
            if i == len(dp) - 1:
                dp[len(dp) - 1] = min(dp[i - 1], dp[i - 2])

        print(dp)
        return dp[len(cost)]


print(Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
