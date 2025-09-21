from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the nums array
        nums.sort()

        res = []

        # iterate over the array - i = 0 to len - 1
        for i in range(len(nums)):
            # check if i greater than 0 and i is equal to i - 1
            if i > 0 and nums[i] == nums[i - 1]:
                # print("here")
                continue
            # we continue with out loop
            # else:
            # once we have our i pointer, we initialize the left and the right pointers
            left, right = i + 1, len(nums) - 1

            # for this i pointer, we will check the values of left and right and get the sum to see if it's equal to 0

            while left < right:
                # calculate the sun at i, left, right
                total = nums[i] + nums[left] + nums[right]
                # if it's 0:
                if total == 0:
                    # add to the res array
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while (
                        left - 1 >= 0
                        and left != right - 1
                        and left < len(nums)
                        and nums[left] == nums[left - 1]
                    ):
                        left += 1
                # if it's less than 0:
                if total < 0:
                    # increase left
                    left += 1
                    while (
                        left - 1 >= 0
                        and left != right - 1
                        and left < len(nums)
                        and nums[left] == nums[left - 1]
                    ):
                        left += 1
                # if it's more than 0:
                if total > 0:
                    # decrease right
                    right -= 1

                    while (
                        right - 1 >= 0
                        and left != right - 1
                        and nums[right] == nums[right - 1]
                    ):
                        right -= 1
        return res


print(Solution().threeSum([0, 0, 0]))
