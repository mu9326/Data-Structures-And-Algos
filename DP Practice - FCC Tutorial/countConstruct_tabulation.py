def countConstruct(target, wordBank):
    # initialize the dp array with default 0 values
    dp = [0 for _ in range(len(target) + 1)]

    # add the seed value
    dp[0] = 1

    # iterate over the dp array
    for i in range(len(dp)):
        # if the value at i is not 0:
        if dp[i] != 0:
            # slice the target starting at i and ending at i + len(word)
            for word in wordBank:
                # if a word matches this sliced string, that means we can reach the word starting from the curr index
                if target[i : i + len(word)] == word:
                    if (i + len(word)) < len(dp):
                        # add the value at dp[i] to dp[i + len(word)]
                        dp[i + len(word)] += dp[i]
    print(dp)
    return dp[len(target)]


print(countConstruct("purple", ["purp", "p", "ur", "le", "purpl", "purple"]))
