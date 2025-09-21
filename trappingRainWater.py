from typing import List
import math


class Solution:
    def trap(self, height: List[int]) -> int:
        # initialize the left and right pointers
        # l, r = 1, 11
        left, right = 0, len(height) - 1

        # initialize the totalWater variable and maxL, maxR, curr variables # mL, mR, curr = 0, 1, 1
        # curr = min(maxL, maxR)
        totalWater = 0
        maxL, maxR = height[left], height[right]
        if maxL <= maxR:
            curr = left
        else:
            curr = right

        while left < right:
            # take the minimum of maxL and maxR and subtract the height at the curr pointer # 1 - 2
            diff = min(maxL, maxR) - height[curr]
            # take the ceiling of this diff and add it to the totalWater variable # 1
            if diff > 0:
                totalWater += diff
            # maxL = max(height[left], maxL) # 2
            maxL = max(height[left], maxL)
            maxR = max(height[right], maxR)  # 1
            if maxL <= maxR:
                # update the left pointer # 3
                left += 1
                # curr = left # 3
                curr = left
            else:
                # update the right pointer
                right -= 1
                curr = right

        return totalWater


print(Solution().trap([4, 2, 0, 3, 2, 5]))
