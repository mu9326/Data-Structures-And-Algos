def countConstruct(target, wordBank):
    if target == "":
        return 1

    # target= "abc" (4)
    count = 0  # ["ab", "a", "c", "b", "abc", "bc"]
    for word in wordBank:  # "bc"
        if target.startswith(word):  # T
            suffix = target[len(word) :]  # ""

            count += countConstruct(suffix, wordBank)  # count = 2

    return count


print(countConstruct("abc", ["ab", "a", "c", "b", "abc", "bc"]))
print(
    countConstruct(
        "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
        ["e", "ee", "eee", "eeeeee", "eeeeeeee", "eeeeeeee"],
    )
)
