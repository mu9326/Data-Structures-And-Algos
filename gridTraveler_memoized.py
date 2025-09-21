def gridTraveler(m, n, memo=None):
    if memo is None:
        memo = {}
    key = (min(m, n), max(m, n))

    if key in memo:
        return memo[key]

    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0

    memo[key] = gridTraveler(m - 1, n, memo) + gridTraveler(m, n - 1, memo)

    return memo[key]


print(gridTraveler(2, 3))
