from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []

        # backtrack function will take 2 arguments -> idx, combination
        def backtrack(idx, combination):
            # base case
            if idx >= len(nums):
                # if the idx >= len
                subsets.append(combination.copy())
                # append the copy of the combination and return
                return

            # recursive case
            # left branch
            combination.append(nums[idx])
            # idx + 1, comb.append(ele)
            backtrack(idx + 1, combination)

            # right branch
            # remove the element from the combination
            combination.pop()
            # idx + 1, comb
            backtrack(idx + 1, combination)

        backtrack(0, [])
        return subsets
