def bestSum(target, nums):
    # initialize the dp array with default None values
    dp = [None for _ in range(target + 1)]

    # add the seed value
    dp[0] = []

    # iterate over the dp array
    for i in range(target + 1):
        if dp[i] is not None:
            curr = dp[i]

            for num in nums:
                if i + num < len(dp):
                    if dp[i + num] is None or (len(curr + [num]) < len(dp[i + num])):
                        dp[i + num] = curr + [num]

    return dp[target]
