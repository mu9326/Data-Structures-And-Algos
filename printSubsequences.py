# Not a leetcode question - just backtracking practice

# Print all subsequences --> a contiguous/non-contiguous sequences in a given order i.e.

# ex. arr = [3, 1, 2]
# result should be in the order -
# [], [2], [1], [1, 2], [3], [3, 2], [3, 1], [3, 1, 2]


def printSubsequences(arr):
    res = []  # [[3, 1, 2], [3, 1]]

    def backtrack(idx, seq):
        if idx >= len(arr):
            res.append(seq.copy())
            return

        # idx = 0, 1, 2
        # consider the element
        backtrack(idx + 1, seq)

        seq.append(arr[idx])

        # skip the element
        backtrack(idx + 1, seq)
        # remove the element from the sequence
        seq.pop()

    backtrack(0, [])

    return res


print(printSubsequences([3, 1, 2]))
