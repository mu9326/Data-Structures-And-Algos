from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack, res = [], []

        def backtrack(openN, closedN):
            # base case
            # if hashmap values are equal to n:
            if openN == closedN == n:
                # append the stack to the res
                res.append("".join(stack))
                return

            # recursive case
            # if any opening brackets are left
            if openN < n:
                # increase the value of the opening bracket in the hashmap
                stack.append("(")
                # add the opening bracket to the stack and recurse
                backtrack(openN + 1, closedN)

                # backtrack
                # pop the opening bracket
                stack.pop()
                # decrease the value of the opening bracket in the hashmap

            # if close < open:
            if closedN < openN:
                # increase the value of the closing bracket in the hashmap
                # add the closing bracket to the stack and recurse
                stack.append(")")

                # backtrack
                # pop the closing bracket
                backtrack(openN, closedN + 1)
                # decrease the value of the closing bracket in the hashmap
                stack.pop()

        backtrack(0, 0)
        return res


print(Solution().generateParenthesis(3))
