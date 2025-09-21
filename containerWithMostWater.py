from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # initialize the left and right pointers to 0 and len - 1
        left, right = 0, len(height) - 1
        res = 0

        while left < right:
            # calculate the area between l and r
            area = (min(height[left], height[right])) * (right - left)
            # update the max area
            res = max(area, res)

            # if height[l] < height[r]:
            if height[left] < height[right]:
                # update l
                left += 1
            else:
                # update r
                right -= 1

        # return max area
        return res
