class Solution:
    # Optimal
    def addStrings2(self, num1: str, num2: str) -> str:
        res = []
        # initialize carry and the indices
        carry = 0
        i, j = len(num1) - 1, len(num2) - 1

        # iterate over both the strings in reverse (while none of the indices is equal to 0)
        while i >= 0 or j >= 0:
            # get the integer equivalent of the digit from the hashmap
            dig1 = ord(num1[i]) - ord("0") if i >= 0 else 0
            dig2 = ord(num2[j]) - ord("0") if j >= 0 else 0
            # add the two digits to the carry
            total = dig1 + dig2 + carry  # 13
            # add this to the res
            res.append(total % 10)  # res = [3, 3, 5, 4]
            carry = total // 10  # carry = 1
            # update the indices
            i -= 1
            j -= 1

        if carry > 0:
            res.append(carry)
        # return the joined operation
        new_str = "".join(str(x) for x in res)  # 3354
        return new_str[::-1]  # 4533

    def addStrings(self, num1: str, num2: str) -> str:
        # "1"
        # "9"

        # res = []
        res = []

        # hard code the str to int hashmap
        str_to_int = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
        }
        # initialize carry and the indices
        carry = 0
        i, j = len(num1) - 1, len(num2) - 1

        # iterate over both the strings in reverse (while none of the indices is equal to 0)
        while i >= 0 and j >= 0:
            # get the integer equivalent of the digit from the hashmap
            # print(str_to_int[num1[i]])
            dig1 = str_to_int[num1[i]]  # 7
            dig2 = str_to_int[num2[j]]  # 5
            # add the two digits to the carry
            total = dig1 + dig2 + carry  # 13
            # add this to the res
            res.append(total % 10)  # res = [3, 3, 5, 4]
            carry = total // 10  # carry = 1
            # update the indices
            i -= 1
            j -= 1

        # add the carry to the remainder of whatever string
        while i >= 0:
            total = str_to_int[num1[i]] + carry  # 4 + 1
            res.append(total % 10)
            carry = total // 10
            i -= 1

        while j >= 0:
            total = str_to_int[num2[j]] + carry
            res.append(total % 10)
            carry = total // 10
            j -= 1

        if carry > 0:
            res.append(carry)

        # return the joined operation
        new_str = "".join(str(x) for x in res)  # 3354
        return new_str[::-1]  # 4533
