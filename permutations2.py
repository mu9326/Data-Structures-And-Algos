from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # initialize the res and the curr array
        res = []

        # def the backtrack function that takes the curr array as an argument
        def backtrack(curr):
            # base case
            # if the curr is equal to nums.length:
            if len(curr) == len(nums):
                # append copy of curr to res
                res.append(curr[:])
                return

            # iterate over the nums array
            for num in nums:  # O(n)
                # if num is not in curr
                if num not in curr:
                    # add it to curr
                    curr.append(num)
                    # backtrack on curr
                    backtrack(curr)
                    # remove it from curr
                    curr.pop()

        # call backtrack on an empty curr array
        backtrack([])
        return res


print(Solution().permute([1, 2, 3]))
