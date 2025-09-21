def canSum(targetSum, numbers):
    # initialize the array to len (targetSum + 1) and populate with F's
    dp = [False] * (targetSum + 1)
    print(dp)

    # initialize the value at 0 to T
    dp[0] = True

    # iterate over the array - # [True, False, True, False, True, False, True, False]
    for i, val in enumerate(dp):  # i = 2
        # if the value is True
        if val:
            # iterate over the nums array # [2, 4]
            for num in numbers:  # 4
                # for each value in the nums array - update the value at the position i + num (num should be within bounds)
                if (i + num) <= targetSum:  # 2 + 4 = 6
                    dp[i + num] = True

    print(dp)
    # return the value at m
    return dp[targetSum]


print(canSum(7, [5, 3, 4, 7]))
print(canSum(7, [2, 4]))
# print(canSum(300, [7, 14]))
