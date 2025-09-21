def allConstruct(target, wordBank):
    # initialize the dp array with [] values
    dp = [[] for _ in range(len(target) + 1)]

    # seed the initial value
    dp[0] = [[]]
    print(dp)

    # iterate over the dp array
    for i in range(len(dp)):
        # if the array at i is not empty:
        if len(dp[i]) != 0:
            # iterate over the word bank
            for word in wordBank:
                # see if there is a word that starts from a letter that represents the current index
                # how do you check that? target[i: i + len(word)] == word
                if target[i : i + len(word)] == word:
                    # if this is true and i + len(word) < len(dp):
                    if i + len(word) < len(dp):
                        # get the value at dp[i] - it's a 2D array
                        # for each [] in dp[i]:
                        for arr in dp[i]:
                            # add the word to it
                            # remember: append() returns None after appending, so temp will be None (either do the following or don't save
                            # anything to a variable after returning and append it in the step below the following)
                            temp = arr + [word]
                            # this whole thing has to be added to the value at dp[i+len(word)]
                            dp[i + len(word)].append(temp)
    print(dp)

    print()
    return dp[len(target)]


print(allConstruct("abc", ["ab", "a", "c", "b", "abc", "bc"]))
