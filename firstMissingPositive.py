from typing import List

# we need to check all values from 1 to len(nums) + 1
# [3, 5, -1, 0]
# [3, 5, -5, -5]

# len(nums) = 4
# default value = len(nums) + 1


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        length = len(nums)
        # first pass
        # update the negative values in nums to have the default val of (len(nums) + 1)
        for i in range(length):
            if nums[i] <= 0 or nums[i] > length:
                nums[i] = length + 1

        # second pass
        # update the values at the respective positions by taking the (abs value + 1)
        for i in range(length):
            num = abs(nums[i])
            if 1 <= num <= length:
                idx = num - 1
                if nums[idx] > 0:
                    nums[idx] = -nums[idx]

        # third pass
        # if the value at a certain index is not negative, we have our answer
        for i in range(length):
            if nums[i] > 0:
                return i + 1

        return length + 1


print(Solution().firstMissingPositive([3, 500, -1, 0, 2, 1]))
