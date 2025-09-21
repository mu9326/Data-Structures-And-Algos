def gridTraveler(m, n):
    # initialize a 2D array with default values
    dp = [[0 for _ in range(m + 1)] for i in range(n + 1)]

    print(dp)

    # add the seed values
    dp[1][1] = 1

    # iterate over the table and add the rest of the values
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # for a particular (m, n) position in the grid
            # add the value at this position to its neighbors - (m+1, n) and (m, n+1)
            if i + 1 <= m:
                dp[i + 1][j] += dp[i][j]
            if j + 1 <= n:
                dp[i][j + 1] += dp[i][j]

    return dp[m][n]


print(gridTraveler(3, 3))
