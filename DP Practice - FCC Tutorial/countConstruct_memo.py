def countConstruct(target, wordBank, memo={}):
    if memo is None:
        memo = {}

    if target in memo:
        return memo[target]

    # if the target is an empty string, return True
    if target == "":
        return 1

    # recursive case
    count = 0
    # iterate over the word bank - O(n)
    for word in wordBank:  # ["a", "d", "", "p"]
        # startsWith() -> O(m) worst case
        if target.startswith(word):
            # remove the prefix from target
            # slicing --> O(k) --> O(m) worst case
            suffix = target[len(word) :]
            # recurse on the resultant string

            # height = m (target), n recursive calls --> n^m
            count += countConstruct(suffix, wordBank, memo)

    memo[target] = count
    return memo[target]


print(countConstruct("abc", ["ab", "a", "c", "b", "abc", "bc"]))
print(
    countConstruct(
        "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
        ["e", "ee", "eee", "eeeeee", "eeeeeeee", "eeeeeeee"],
    )
)
