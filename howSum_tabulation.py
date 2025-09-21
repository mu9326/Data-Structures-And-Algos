def howSum(targetSum, numbers):
    # initialize the dp array to targetSum + 1 - all values will be None
    dp = [None] * (targetSum + 1)

    # value at 0 will be []
    dp[0] = []
    # for each value in the dp array:
    for i in range(targetSum + 1):
        if dp[i] is not None:
            for num in numbers:
                if i + num <= targetSum:
                    new_comb = [comb + [num] for comb in dp[i]]
                    if dp[i + num] is None:
                        dp[i + num] = new_comb
                    else:
                        dp[i + num].extend(new_comb)

    print(dp)
    if dp[targetSum]:
        return dp[targetSum][0]  # any one combination
    return None


print(howSum(7, [5, 3, 4, 7]))
# print(howSum(7, [2, 4]))
# print(howSum(300, [7, 14]))
