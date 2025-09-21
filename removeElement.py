from typing import List

# [2, 2, 2, 2, _, _, _, _]


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # initialize the two pointers
        left, right = 0, 0
        counter = 0

        while right < len(nums):
            if nums[right] != val:
                # swap nums at left and right
                nums[left], nums[right] = nums[right], nums[left]
                # counter += 1
                counter += 1
                # left += 1
                left += 1
            # else:
            else:
                # change the value at nums to be '_'
                nums[right] = "_"
            # right += 1
            right += 1

        return counter

    def removeElement2(self, nums, val):
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k
