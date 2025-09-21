class Solution:
    def climbStairs(self, n: int) -> int:
        def dp(n, memo):
            if n in memo:
                return memo[n]

            if n < 0:
                return 0

            if n == 0:
                return 1

            memo[n] = dp(n - 1, memo) + dp(n - 2, memo)

            return memo[n]

        return dp(n, {})

    def climbStairs2(self, n):
        # initialize the dp array with default values
        dp = [0 for _ in range(n + 1)]

        # seed the initial value
        dp[0] = 1

        # iterate over the dp array
        for i in range(len(dp)):
            # if the value at i is not 0:
            if dp[i] != 0:
                # if i + 1 < len(dp)
                if i + 1 < len(dp):
                    # look one place ahead in the array and add dp[i] to the value at that position
                    dp[i + 1] += dp[i]
                if i + 2 < len(dp):
                    # look two places ahead in the array and add dp[i] to the value at that position
                    dp[i + 2] += dp[i]

        return dp[n]


print(Solution().climbStairs2(5))
