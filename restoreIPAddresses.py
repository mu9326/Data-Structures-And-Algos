from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        if len(res) > 12:
            return []

        def backtrack(i, dots, curIP):
            # success base case: if we have reached the limit for dots or if we have reached the end of the string
            if dots == 4 and i == len(s):
                # add the currIP to the res (but remove the 4th dot first)
                res.append(curIP[:-1])
                return

            # failure base case: if we have exceeded the number of dots or we have reached the end of string
            if dots > 4 or i > len(s):
                return

            # the dots should be in the range (curr index, curr index + 3)
            # we take the minimum of i + 3 and len(s) to make sure the index does not go out of bounds
            for j in range(i, min(i + 3, len(s))):
                # check if the number from i to j is less than 255 and check if there are no leading zeroes
                if int(s[i : j + 1]) < 256 and (i == j or s[i] != "0"):
                    # backtrack if it's a valid integer
                    backtrack(j + 1, dots + 1, curIP + s[i : j + 1] + ".")

        backtrack(0, 0, "")
        return res
