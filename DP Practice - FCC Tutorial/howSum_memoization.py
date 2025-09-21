def howSum(target, nums, memo=None):
    if not memo:
        memo = {}

    if target in memo:
        return memo[target]

    if target < 0:
        return None

    if target == 0:
        return []

    for num in nums:
        res = howSum(target - num, nums, memo)
        if res:
            res = res + [num]
            memo[target] = res
            return memo[target]

    memo[target] = None
    return None
