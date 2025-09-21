class Solution:
    def climbStairs(self, n: int) -> int:
        prev, prev2 = 2, 1
        curr = 0
        # iterate from 0 to n -->
        for _ in range(3, n + 1):
            # recurrence relation
            curr = prev + prev2
            # S[n] = S[n - 1] + S[n - 2]
            # update prev2 to prev
            prev2 = prev
            # update prev to curr
            prev = curr

        return prev


print(Solution().climbStairs(5))
