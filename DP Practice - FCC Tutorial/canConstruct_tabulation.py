def canConstruct(target, wordBank):
    dp = [False for _ in range(len(target) + 1)]

    dp[0] = True

    for i in range(len(dp)):
        if dp[i] is True:
            for word in wordBank:
                if target[i : i + len(word)] == word:
                    if i + len(word) < len(dp):
                        dp[i + len(word)] = True

    print(dp)
    return dp[len(target)]


print(canConstruct("abcdef", ["ab", "abc", "cd", "defter", "abcd"]))
