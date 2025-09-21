def canSum(target, nums, memo=None) -> bool:
    if not memo:
        memo = {}

    if target in memo:
        return memo[target]
    # base cases -
    # 1. if my target is less than 0
    if target < 0:
        return False
    # 2. if my target is 0
    if target == 0:
        return True

    # recursive
    for num in nums:
        if canSum(target - num, nums):
            memo[target] = True
            return True

    memo[target] = False
    return False
