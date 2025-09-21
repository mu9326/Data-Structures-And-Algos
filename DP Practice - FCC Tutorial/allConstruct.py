def allConstruct(target, wordBank):
    if target == "":
        return [[]]

    res = []

    for word in wordBank:
        if target.startswith(word):
            suffix = target[len(word) :]

            suffix_ways = allConstruct(suffix, wordBank)

            for way in suffix_ways:
                res.append(way + [word])

    return res
