from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # len(nums) = 0? No
        # unique integers

        # [1, 2, 3]

        # [[subsets]], no duplicates
        # [[], [1], [2], [3], [1, 2], [1, 3], [1, 4], [2, 3],[1, 2, 3]]

        res = []

        # recursive function
        def backtrack(idx, subset):
            # backtrack(index, subset)
            if idx >= len(nums):
                # base case:
                # if idx is out of range:
                # append the subset to the res array
                res.append(subset[:])
                return

            # recursive case
            # include
            # append the element to the curr subset
            subset.append(nums[idx])
            # we explore what happens when we include this - call our function with updated index (the next index) and updated subset
            backtrack(idx + 1, subset)

            # exclude
            # we remove the ele from the curr subset
            subset.pop()
            # we explore next - recursive function with updated index and original subset
            backtrack(idx + 1, subset)

        # call our backtrack function (initially)
        backtrack(0, [])
        # return the res
        return res


print(Solution().subsets([1, 2, 3]))
