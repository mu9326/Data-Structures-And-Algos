from typing import List


class Solution:
    # recursive solution
    def canJump(self, nums: List[int]) -> bool:
        # [2, 3, 1, 1, 4]

        # def recurse(index)
        def recurse(index, memo):
            # base case:
            # if index is equal to the len(nums) - 1:
            if index in memo:
                return memo[index]

            if index == len(nums) - 1:
                return True

            # recursive case
            # iterate over the value nums[index]
            for i in range(1, nums[index] + 1):
                # if recurse(index + i):
                print("Recursing on index: ", index + i)
                if recurse(index + i, memo):
                    memo[index] = True
                    return memo[index]

            memo[index] = False
            return memo[index]

        memo = {}
        return recurse(0, memo)

    # Greedy solution
    def canJump2(self, nums: List[int]) -> bool:
        # [1, 2, 3, 1, 1, 1, 0, 5]
        # initialize the maxIndex variable
        maxIndex = 0

        # iterate over the nums array
        for i in range(len(nums)):
            if maxIndex < i:
                return False
            if nums[i] + i > maxIndex:
                # update maxIndex
                maxIndex = nums[i] + i
            if maxIndex >= len(nums):
                return True

        return True


print(Solution().canJump2([3, 2, 1, 0, 4]))
print(Solution().canJump2([2, 3, 1, 1, 4]))
print(Solution().canJump2([1, 2, 4, 1, 1, 0, 2, 5]))
