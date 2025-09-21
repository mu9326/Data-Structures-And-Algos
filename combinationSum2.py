from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        # initialize a res variable
        res = []

        # backtrack function
        def backtrack(idx, target, combination):
            # base cases
            # if the value at idx is equal to the target value
            if target == 0:
                # res.append(combination)
                res.append(combination.copy())
                return
            # if the value at idx is less than the target value
            if idx >= len(candidates) or target < 0:
                return

            # left branch
            # index + 1, target - candidates[index], comb.append(candidates[index])
            # print("idx before the left branch: ", idx)
            combination.append(candidates[idx])
            backtrack(idx + 1, target - candidates[idx], combination)

            # comb.pop
            combination.pop()

            # right branch
            # print("idx: ", idx)
            i = idx + 1
            # print("i: ", i)
            # print("i - 1: ", i - 1)
            while (
                i - 1 >= 0
                and i < len(candidates)
                and candidates[i] == candidates[i - 1]
            ):
                i += 1
            backtrack(i, target, combination)

        backtrack(0, target, [])
        return res


print(Solution().combinationSum2([10, 1, 6, 7, 5, 2, 1], 8))
