def gridTraveler(m, n):
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    dp[1][1] = 1

    # for each row index:
    for i in range(m + 1):
        # for each col index:
        for j in range(n + 1):
            curr = dp[i][j]
            # update the bottom position (if within bounds)
            if (i + 1) <= m:
                dp[i + 1][j] += curr
            # update the right position (if within bounds)
            if (j + 1) <= n:
                dp[i][j + 1] += curr

    return dp[m][n]


print(gridTraveler(18, 18))
