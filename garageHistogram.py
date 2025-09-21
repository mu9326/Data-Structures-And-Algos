def garage_histogram(tickets, length):
    res = [0] * length
    for entry, exit in tickets:
        for t in range(entry, exit):
            if t < length:
                res[t] += 1
    return res


# Example usage:
tickets = [(1, 3), (2, 4), (2, 3)]
length = 6
print(garage_histogram(tickets, length))  # Output: [0, 1, 3, 2, 2, 1]
