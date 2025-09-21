from typing import List


class Solution:
    # Top Down Approach
    def rob(self, nums: List[int]) -> int:
        def dp(index, memo):
            if index in memo:
                return memo[index]
            # if index is out of bounds:
            if index >= len(nums):
                return 0

            memo[index] = max(nums[index] + dp(index + 2), dp(index + 1))
            return memo[index]

        memo = {}
        return dp(0, memo)

    # Bottom-Up approach
    def rob2(self, nums: List[int]) -> int:
        # initialize the dp array with default values
        dp = [0 for _ in range(len(nums))]

        # add the seed values
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        # iterate over the array
        for i in range(2, len(dp)):
            # at each position in the array, we have two choices - to not choose the curr position i.e. stick to the value at i - 1
            # or choose the curr position (nums[i] + value at 1 - 2) -- we choose the maximum of the two results
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[len(nums) - 1]


print(Solution().rob2([1, 2, 3, 1]))
