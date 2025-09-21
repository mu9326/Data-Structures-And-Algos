from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = 0

        for num in nums:
            if curSum < 0:
                curSum = 0

            curSum += num
            maxSum = max(maxSum, curSum)

        return maxSum

    def maxSubArray2(self, nums: List[int]) -> int:
        def dfs(i, flag):
            print(f"dfs({i}, {flag}) called")
            if i == len(nums):
                return 0 if flag else -1e6
            if flag:
                res = max(0, nums[i] + dfs(i + 1, True))
            else:
                res = max(dfs(i + 1, False), nums[i] + dfs(i + 1, True))
            print(f"dfs({i}, {flag}) returns {res}")
            return res

        return dfs(0, False)


print(Solution().maxSubArray2([-2, 7, -3, 4]))
