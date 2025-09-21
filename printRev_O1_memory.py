# Print a string in reverse order recursively

# Two Pointer approach
def printReverse(str_arr):
    # initialize the two pointers
    left, right = 0, len(str_arr) - 1

    while left < right:
        # swap the elements at left and right
        str_arr[left], str_arr[right] = str_arr[right], str_arr[left]
        left += 1
        right -= 1

    # return the input string
    return str_arr


# Recursive Approach


def printReverse2(str_arr):
    def helper(left, right):
        # base case
        if left >= right:
            return

        # recursive case
        # swap the chars at left and right
        str_arr[left], str_arr[right] = str_arr[right], str_arr[left]
        # recurse on left + 1 and right - 1
        helper(left + 1, right - 1)

    helper(0, len(str_arr) - 1)
    return str_arr


print(printReverse(["h", "e", "l", "l", "o"]))
print(printReverse2(["h", "e", "l", "l", "o"]))
