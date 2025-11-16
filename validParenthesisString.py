class Solution:
    def checkValidString(self, s: str) -> bool:
        memo = {}

        # define the backtracking function:
        # def backtrack(index, openN, closeN):
        def backtrack(idx, openN, closedN):
            # base cases

            if (idx, openN, closedN) in memo:
                return memo[(idx, openN, closedN)]

            if openN < closedN:
                memo[(idx, openN, closedN)] = False
                return False

            if idx >= len(s):
                result = openN == closedN
                memo[(idx, openN, closedN)] = result
                return result

            # recursive case
            # check the char at the current index:
            # if the char is '(':
            if s[idx] == "(":
                # increase the openN count and idx + 1 and call the recursive function
                result = backtrack(idx + 1, openN + 1, closedN)
            # elif the char is ')':
            elif s[idx] == ")":
                # increase the closeN count and idx + 1 and call the recursive function
                result = backtrack(idx + 1, openN, closedN + 1)
            # elif it's '*':
            elif s[idx] == "*":
                # if any of these return True:
                # ( check if any of the backtracking functions return true
                result = (
                    backtrack(idx + 1, openN + 1, closedN)
                    or backtrack(idx + 1, openN, closedN + 1)
                    or backtrack(idx + 1, openN, closedN)
                )

            memo[(idx, openN, closedN)] = result
            return result

        return backtrack(0, 0, 0)


print(Solution().checkValidString("*)(*))("))
