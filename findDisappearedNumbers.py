from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # [4,3,2,7,8,2,3,1]
        res = []
        # iterate over the array and for each element mark the corresponding index as negative

        for i in range(len(nums)):  # i = 1
            val = abs(nums[i])  # val = nums[1] = 3

            if nums[val - 1] < 0:
                # if it's already negative, don't do anything
                continue
            nums[val - 1] = -1 * nums[val - 1]  # - 2

        # iterate over the array once more to check for negatives and add the positive indices to the res array
        print(nums)
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i + 1)

        return res
