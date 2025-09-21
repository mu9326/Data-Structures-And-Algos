from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        # iterate over the nums array (i)
        for i in range(len(nums)):
            # initialize left at i + 1 and right at len(nums) - 1
            left, right = i + 1, len(nums) - 1
            while left < right:
                # check if i + l + r == 0
                total = nums[i] + nums[left] + nums[right]
                # if it is equal to 0:
                if total == 0:
                    # append the triplets to res
                    res.append([nums[i], nums[left], nums[right]])
                    # update the left pointer (but check that the values are not the same as the prev left pointer)
                    left += 1
                    while left < len(nums) and nums[left] == nums[left - 1]:
                        left += 1
                # if the sum < 0:
                elif total < 0:
                    # update the left pointer
                    left += 1
                # if the sum > 0:
                else:
                    # update the right pointer
                    right -= 1

            # update the i pointer until it's not equal to prev i
            i += 1
            while i < len(nums) and nums[i] == nums[i - 1]:
                i += 1

        return res


print(Solution().threeSum([-4, -1, -1, 0, 1, 2]))
