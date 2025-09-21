def bestSum(targetSum, numbers, memo={}):
    if memo is None:
        memo = {}

    if targetSum in memo:
        return memo[targetSum]

    if targetSum == 0:
        return []

    if targetSum < 0:
        return None

    shortestCombination = None  # 2

    # (8, [2, 3, 5])

    # recursive case
    for num in numbers:
        # print("num: ", num)  # 3
        remainder = targetSum - num  # 6 - 2 = 4 - 2
        remainderResult = bestSum(remainder, numbers)  # 6 -> 4
        if remainderResult is not None:
            path = remainderResult + [num]  # [2, 2]
            # if the shortestCombination is None:
            if not shortestCombination or (len(path) < len(shortestCombination)):
                shortestCombination = path  # [2]
                # print("shortestCombination: ", shortestCombination)
        # return shortestCombination

    memo[targetSum] = shortestCombination
    return shortestCombination  # [2]


print(bestSum(7, [5, 3, 4, 7]))
print(bestSum(8, [2, 3, 5]))
print(bestSum(8, [1, 4, 5]))
# print(bestSum(100, [1, 2, 5, 25]))
