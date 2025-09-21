def canSum(target, nums, memo=None):
    # base cases:
    if memo is None:
        memo = {}
    # targetSum == 0 -> True
    if target in memo:
        return memo[target]
    if target == 0:
        return True
    # targetSum < 0 -> False
    if target < 0:
        return False

    # recursive case
    for num in nums:
        if (canSum(target - num, nums, memo)) is True:
            memo[target] = True
            return True
    # target gets updated for each value in nums
    memo[target] = False
    return False


print(canSum(7, [5, 3, 4, 7]))
print(canSum(7, [2, 4]))
print(canSum(300, [7, 14]))
