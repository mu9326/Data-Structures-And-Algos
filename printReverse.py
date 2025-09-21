# Print a string in reverse order recursively


def printReverse(string):
    # initialize a new_string variable
    new_string = ""

    def helper(string, new_string):
        # base case
        # if the string is empty
        if len(string) == 0:
            return new_string

        # print the char at index -1
        new_string += string[-1]  # new_string = 'y'

        # call the recursive function with the sliced str
        return helper(string[: len(string) - 1], new_string)

    # recursive function call
    return helper(string, new_string)


print(printReverse("July"))
