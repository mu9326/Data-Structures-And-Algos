from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # initialize the dp array of len(target + 1) with default infinity values
        dp = [float("inf") for _ in range(amount + 1)]
        # print(dp)
        # seed the value for 0
        dp[0] = 0

        # iterate over the dp array:
        for i in range(amount + 1):
            # if the value at i is not equal to inf:
            if dp[i] != float("inf"):
                # get the value at this position (minCoins) and add 1 to it bcz you'd be using one extra
                # coin of each denomination to reach to the next value
                minCoins = dp[i] + 1
                # iterate over the coins array
                for j in coins:
                    # if the value at coins[j] + i has a value greater than minCoins
                    # update it to minCoins
                    if i + j < len(dp):
                        dp[i + j] = min(minCoins, dp[i + j])

        if dp[amount] != float("inf"):
            return dp[amount]
        else:
            return -1


print(Solution().coinChange([1, 2, 5], 11))
