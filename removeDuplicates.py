from typing import List

# Notes -
# Make notes on the approach
# T. C. -> O(2.n) --> O(n)


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # [0, 1, 2, 3, 4, 2, 2, 3, 3, 4]
        # initialize the left and right pointers at index 1
        # l, r = 5, 10
        left, right = 1, 1

        # while right is not out of bounds
        while right < len(nums):
            # if val at right is not equal to val at right-1
            if nums[right] != nums[right - 1]:
                # update the val at left with the val at right
                nums[left] = nums[right]
                # increase left
                left += 1

            # increase right
            right += 1

        print(nums)
        # return the left index
        return left

    # edge cases:
    # 1. Can nums be empty or non-sorted?
    # 2. Nums has only one element


print(Solution().removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
