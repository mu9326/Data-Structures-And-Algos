from collections import deque


# USING A LIST
def process_string(s: str) -> str:
    chars = []
    reversed_flag = False

    for ch in s:
        if "a" <= ch <= "z":  # letter
            if reversed_flag:
                chars.insert(0, ch)  # O(n) — could optimize with deque
            else:
                chars.append(ch)

        elif ch == "*":
            if chars:
                if reversed_flag:
                    chars.pop(0)
                else:
                    chars.pop()

        elif ch == "#":
            chars = chars + chars

        elif ch == "%":
            reversed_flag = not reversed_flag

    if reversed_flag:
        chars.reverse()
    return "".join(chars)


# USING A DEQUE
def process_string2(s: str) -> str:
    chars = deque()
    reversed_flag = False

    for ch in s:
        if "a" <= ch <= "z":
            if reversed_flag:
                chars.appendleft(ch)
            else:
                chars.append(ch)

        elif ch == "*":
            if chars:
                if reversed_flag:
                    chars.popleft()
                else:
                    chars.pop()

        elif ch == "#":
            chars.extend(chars)

        elif ch == "%":
            reversed_flag = not reversed_flag

    if reversed_flag:
        chars.reverse()
    return "".join(chars)


print(process_string("a#bbe%c%%%def%#"))
