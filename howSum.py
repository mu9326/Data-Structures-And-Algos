def howSum(targetSum, nums):
    if targetSum == 0:
        return []

    if targetSum < 0:
        return None

    # recursive case
    for num in nums:  # ["5", "3", 4, 7]
        remainder = targetSum - num  # 7 - 3 = 4 - 4
        remainderResult = howSum(remainder, nums)  # []
        if remainderResult is not None:
            return remainderResult + [num]  #

    return None


print(howSum(7, [5, 3, 4, 7]))
print(howSum(7, [2, 4]))
# print(howSum(300, [7, 14]))
