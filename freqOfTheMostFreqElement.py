from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # initialize the left and right pointers
        left, right = 0, 0

        # initialize the total and res variables
        total, res = 0, 0

        nums.sort()

        # begin the sliding window -
        # while r < len(nums):
        while right < len(nums):
            # add nums[r] to the total
            total += nums[right]

            # check out condition - # if the window is invalid:
            # shrink the window
            while (nums[right] * (right - left + 1)) > (total + k):
                # decrease the total by nums[l]
                total -= nums[left]
                # increase the left pointer
                left += 1

            res = max(res, (right - left + 1))
            right += 1

        return res


print(Solution().maxFrequency([4, 2, 1, 1, 2, 1], 2))
