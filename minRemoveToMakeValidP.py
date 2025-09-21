class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # initialize count, stack
        count = 0
        stack = []

        # iterate over the array:
        for c in s:
            # if the char is an open parenthesis:
            if c == "(":
                count += 1
            # if it's closed:
            if c == ")":
                count -= 1
            if count < 0 and c == ")":
                # append the char to the stack
                count += 1
            else:
                stack.append(c)

        # print(stack)

        # # iterate over the array backwards:
        for i in range(len(stack) - 1, -1, -1):
            if count != 0:
                if stack[i] == "(":
                    stack.pop(i)
                    count -= 1

        return "".join(stack)

    def minRemoveToMakeValid2(self, s: str) -> str:
        # initialize stack, openN, closedN
        stack = []
        openN = 0
        closedN = 0

        # iterate over the string
        for i in range(len(s)):
            # if the char is '(':
            if s[i] == "(":
                # increase the openN count
                openN += 1
            # if the char is ')':
            if s[i] == ")":
                # increase the closedN count
                closedN -= 1
            # if closedN <= openN:
            if closedN <= openN:
                # add the curr char to the stack
                stack.append(s[i])

            print(stack)

        # once the iteration is over:
        # while openN > closedN:
        # iterate over the stack in reverse:
        # remove the openN parenthesis
        # decrease the openN count

        # return "".join(stack)

        pass


print(Solution().minRemoveToMakeValid("lee(tcode))))("))
