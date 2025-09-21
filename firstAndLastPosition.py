from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        lastIdx = -1
        startIdx = -1

        while left <= right:
            mid = left + ((right - left) // 2)
            if nums[mid] == target:
                lastIdx = mid
                left += 1
            elif nums[mid] > target:
                right -= 1
            else:
                left += 1

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + ((right - left) // 2)
            if nums[mid] == target:
                startIdx = mid
                right -= 1
            elif nums[mid] > target:
                right -= 1
            else:
                left += 1

        return [startIdx, lastIdx]
