from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(idx, target, combination):
            # base case
            # if the value at idx is less than the target value
            if idx >= len(candidates) or target < 0:
                return
            # if the value at idx is equal to the target value
            if target == 0:
                # res.append(combination)
                res.append(combination.copy())
                return

            # recursive case
            # include the current idx
            combination.append(candidates[idx])
            backtrack(idx, target - candidates[idx], combination)
            combination.pop()
            # exclude the current idx
            backtrack(idx + 1, target, combination)

        backtrack(0, target, [])
        return res


solution = Solution()
print(solution.combinationSum2([1, 2, 2, 2, 5], 5))
