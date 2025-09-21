def howSum(target, nums):
    # initialize the dp array with default None values
    dp = [None for _ in range(target + 1)]

    # seed the initial value
    dp[0] = []

    # iterate over the array
    for i in range(target + 1):
        # if the value at the position is not None:
        if dp[i] is not None:
            # iterate over nums
            for num in nums:
                # at position i + nums (if within bounds), copy the value at i and add nums to it
                if i + num < len(dp):
                    dp[i + num] = dp[i] + [num]

    # return the ans
    return dp[target]


print(howSum(7, [5, 3, 4, 7]))
print(howSum(7, [2, 4]))
