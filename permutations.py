from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []  # []

        def backtrack(idx, nums):
            if idx >= len(nums):
                res.append(nums)

            for i in range(idx, len(nums)):
                nums_copy = nums[:]
                print("nums_copy before the swap: ", nums_copy)
                print("Swapping ", nums_copy[idx], "and ", nums_copy[i])
                nums_copy[idx], nums_copy[i] = nums_copy[i], nums_copy[idx]
                print("nums_copy after the swap: ", nums_copy)
                print()
                backtrack(idx + 1, nums_copy)

        backtrack(0, nums)
        return res


print(Solution().permute([1, 2, 3]))
