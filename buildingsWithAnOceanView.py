from typing import List


class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        # heights = [4, 2, 3, 1, 5]
        stack = []  # [5]
        res = []  # [4]

        for i, h in enumerate(heights):
            while stack and h >= stack[-1]:
                stack.pop()
                res.pop()
            stack.append(h)
            res.append(i)

        return res


print(Solution().findBuildings([2, 2, 2]))
