from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # [1, 1, 1, 2, 2, 2, 3, 3]

        left, right = 0, 0
        count = 1
        while right < len(nums):
            while nums[right] != nums[right - 1]:
                count += 1

                if count <= 2:
                    nums[left] = nums[right]
                left += 1
                right += 1

            right += 1

        return left


print(Solution().removeDuplicates([1, 1, 1, 2, 2, 2, 3, 3]))
