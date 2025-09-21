# Question3: Given a string expression. Evaluate the expression. Return an integer that represents the value of the expression.
# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# Input = "(3+2)*2"
# Output = 10
# Note: This is different from the question 'Evaluate Reverse Polish Notation'


def evaluate_expression1(expr: str) -> int:
    # stack = [3]
    # (3 + 2) * 2
    # sign = '+'
    # num = 2
    def helper(s, i=0):
        stack = []
        num = 0
        sign = "+"

        while i < len(s):
            ch = s[i]  # +

            if ch.isdigit():
                num = num * 10 + int(ch)  # num = 0 * 10 + 2

            if ch == "(":
                num, i = helper(s, i + 1)  # evaluate sub-expression

            # If operator or end of expression
            if (not ch.isdigit() and ch != " ") or i == len(s) - 1:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop() * num)
                elif sign == "/":
                    prev = stack.pop()
                    # Truncate toward zero
                    stack.append(int(prev / num))

                num = 0
                sign = ch

            if ch == ")":
                return sum(stack), i

            i += 1

        return sum(stack), i

    result, _ = helper(expr.replace(" ", ""))
    return result


# Example
print(evaluate_expression1("(3+2)*2"))  # Output: 10
print(evaluate_expression1("3+5/2"))  # Output: 5 (since truncation toward zero)
print(evaluate_expression1("10/(3-1)"))  # Output: 5


# Convert to ERPN
def to_rpn(expr: str):
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2}
    output = []
    ops = []
    num = ""

    for ch in expr:
        if ch.isdigit():
            num += ch
        else:
            if num:
                output.append(int(num))
                num = ""
            if ch in precedence:
                while (
                    ops
                    and ops[-1] in precedence
                    and precedence[ops[-1]] >= precedence[ch]
                ):
                    output.append(ops.pop())
                ops.append(ch)
            elif ch == "(":
                ops.append(ch)
            elif ch == ")":
                while ops and ops[-1] != "(":
                    output.append(ops.pop())
                ops.pop()

    if num:
        output.append(int(num))
    while ops:
        output.append(ops.pop())
    return output


def eval_rpn(tokens):
    stack = []
    for token in tokens:
        if isinstance(token, int):
            stack.append(token)
        else:
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                # Truncate toward zero
                stack.append(int(a / b))
    return stack[0]


def evaluate_expression(expr: str) -> int:
    rpn = to_rpn(expr.replace(" ", ""))
    return eval_rpn(rpn)


# Examples
print(evaluate_expression("(3+2)*2"))  # 10
print(evaluate_expression("3+5/2"))  # 5
print(evaluate_expression("10/(3-1)"))  # 5
print(evaluate_expression("14-3/2"))  # 13 (since 3/2 = 1, trunc toward zero)
