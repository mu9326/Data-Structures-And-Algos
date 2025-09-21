def bestSum(targetSum, numbers):
    dp = [None] * (targetSum + 1)
    dp[0] = []

    for i in range(targetSum + 1):
        if dp[i] is not None:
            for num in numbers:
                if i + num <= targetSum:
                    new_combination = dp[i] + [num]
                    if dp[i + num] is None or len(new_combination) < len(dp[i + num]):
                        dp[i + num] = new_combination

    return dp[targetSum]


print(bestSum(7, [5, 3, 4, 7]))
print(bestSum(8, [2, 3, 5]))
print(bestSum(8, [1, 4, 5]))
print(bestSum(100, [1, 2, 5, 25]))
