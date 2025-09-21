def allConstruct(target, wordBank):
    if target == "":
        return [[]]

    res = []
    # iterate over the wordBank
    for word in wordBank:
        # for each word that is a prefix of the target:
        if target.startswith(word):  # O(m)
            # get the suffix
            suffix = target[len(word) :]  # O(m)

            # recurse on the suffix and store the res in a variable
            suffix_ways = allConstruct(suffix, wordBank)  # O(n ^ m)

            # iterate over the elements of this temp variable
            for way in suffix_ways:
                # for each element, add the current word to it
                # store the above in the res array
                res.append([word] + way)

    return res


print(allConstruct("abc", ["ab", "a", "c", "b", "abc", "bc"]))
print(
    allConstruct(
        "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
        ["e", "ee", "eee", "eeeeee", "eeeeeeee", "eeeeeeee"],
    )
)
