def gridTraveler(m, n):
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0

    return gridTraveler(m - 1, n) + gridTraveler(m, n - 1)
