def canConstruct(target, wordBank, memo={}):
    if memo is None:
        memo = {}

    if target in memo:
        return memo[target]
    # if the target is an empty string, return True
    if target == "":
        return True

    # recursive case
    # iterate over the word bank - O(n)
    for word in wordBank:  # ["a", "d", "", "p"]
        if word == "":
            continue
        # startsWith() -> O(m) worst case
        if target.startswith(word):
            # remove the prefix from target
            # slicing --> O(k) --> O(m) worst case
            suffix = target[len(word) :]
            # recurse on the resultant string

            # height = m (target), n recursive calls --> n^m
            if canConstruct(suffix, wordBank):
                memo[target] = True
                return True
    memo[target] = False
    return False


print(canConstruct("app", ["a", "d", "", "p"]))  # true
print(canConstruct("lap", ["al", "d", "", "p"]))  # false
print(canConstruct("app", ["a", "d", "", "p"]))  # true
print(canConstruct("", ["rat", "cat", "mouse"]))  # true
