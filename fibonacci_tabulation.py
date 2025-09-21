def fib(n):
    dp = [0] * (n + 1)

    dp[0], dp[1] = 0, 1

    for i in range(len(dp) - 2):
        dp[i + 1] += dp[i]
        dp[i + 2] += dp[i]

    dp[len(dp) - 1] += dp[len(dp) - 2]

    return dp[n]


print(fib(10))
