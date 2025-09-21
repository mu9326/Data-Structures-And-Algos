def canSum(target, nums) -> bool:
    # initialize the array of length target with default F values
    dp = [False for _ in range(target + 1)]

    # seed the value at index 0
    dp[0] = True

    # iterate over the array to update values that can be reached from the current value (which needs to be true)
    for i in range(len(dp)):
        if dp[i] is True:
            for n in nums:
                if i + n < len(dp):
                    dp[i + n] = True

    return dp[target]


print(canSum(7, [5, 3, 4]))
print(canSum(7, [5, 3, 4, 7]))
print(canSum(7, [2, 4]))
print(canSum(300, [7, 14]))
