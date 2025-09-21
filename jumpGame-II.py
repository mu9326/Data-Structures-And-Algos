from typing import List


class Solution:
    # recursive solution
    def jump(self, nums: List[int]) -> int:
        # [2, 3, 1, 1, 4]
        # i = 0
        if len(nums) == 0:
            return 1

        memo = {}

        # recurse function(index):
        def recurse(index, memo):
            if index in memo:
                return memo[index]
            # base case
            if index == len(nums) - 1:
                return 0

            # minWays = + inf
            minWays = float("inf")

            # for i in range(1, nums[index] + 1):
            for i in range(1, nums[index] + 1):
                if index + i < len(nums):
                    # recurse on index + i
                    minWays = min(minWays, recurse(index + i, memo))

            memo[index] = 1 + minWays
            return memo[index]

        return recurse(0, memo)

    def jump2(self, nums: List[int]) -> int:
        # initialize the left, right pointers
        left, right = 0, 0
        # initialize the jumps
        jumps = 0

        while right < len(nums) - 1:
            # initialize the farthest variable
            farthest = 0

            # for nums from left to right:
            for i in range(left, right + 1):
                farthest = max(farthest, i + nums[i])
                # get the farthest num

            left = right + 1
            right = farthest
            # increase jumps
            jumps += 1

        # return jumps
        return jumps


print(Solution().jump2([2, 3, 1, 1, 4]))
print(Solution().jump2([0]))
print(Solution().jump2([2, 1]))
