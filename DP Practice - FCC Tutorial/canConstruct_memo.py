def canConstruct(target, wordBank, memo=None):
    if not memo:
        memo = {}

    if target in memo:
        return memo[target]

    if target == "":
        return True

    for word in wordBank:
        if word == "":
            continue

        if target.startswith(word):
            suffix = target[len(word) :]

        if canConstruct(suffix, wordBank):
            memo[target] = True
            # return memo[suffix]
            return True

    memo[target] = False
    return False
