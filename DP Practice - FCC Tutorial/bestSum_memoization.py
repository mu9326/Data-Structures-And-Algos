def bestSum(target, nums, memo):
    if target < 0:
        return None

    if target == 0:
        return []

    shortest = None

    for num in nums:
        res = bestSum(target - num, nums)
        if res:
            res = res + [num]
            if not shortest or len(res) < len(shortest):
                shortest = res

    return shortest
