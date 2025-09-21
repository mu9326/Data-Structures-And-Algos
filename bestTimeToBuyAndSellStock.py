from typing import List

# Make notes on the approach


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # initialize the pointers and maxProfit
        left, right = 0, 1
        maxProfit = 0

        while right < len(prices):
            if prices[left] > prices[right]:
                # update left
                left = right
            # update maxProfit
            maxProfit = max(maxProfit, prices[right] - prices[left])
            right += 1

        return maxProfit


print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
