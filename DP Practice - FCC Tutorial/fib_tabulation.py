def fib(n):
    # initialize the table with default values
    dp = [0 for _ in range(n + 1)]

    # add the seed values
    dp[0], dp[1] = 0, 1

    # iterate over the table and fill out the values
    for i in range(len(dp) - 2):
        dp[i + 1] += dp[i]
        dp[i + 2] += dp[i]

    dp[n] += dp[n - 1]

    return dp[n]


print(fib(6))
print(fib(8))
print(fib(10))
