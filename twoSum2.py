from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # initialize the two pointers
        left, right = 0, len(numbers) - 1

        # iterate over the array in such a way that left < right
        while left < right:
            # if the sum of left and right values == target:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left + 1, right + 1]
                # return the indices
            elif total > target:
                right -= 1
            else:
                left += 1
