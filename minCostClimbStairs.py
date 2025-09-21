from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def dp(index):
            if index == 0 or index == 1:
                return cost[index]

            if index < 0:
                return 0

            return cost[index] + (min(dp(index - 1), dp(index - 2)))

        return min(dp(len(cost) - 1), dp(len(cost) - 2))


print(Solution().minCostClimbingStairs([10, 15, 5, 30, 4, 4, 10]))
