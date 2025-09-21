from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        prefix = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[0 : len(prefix) - 1]
                if prefix == "":
                    return ""
        return prefix


# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         res = ""

#         for i in range(len(strs[0])):
#             for s in strs:
#                 if i == len(s) or s[i] != strs[0][i]:
#                     return res
#             res += strs[0][i]

#         return res


print(Solution().longestCommonPrefix(["flower", "flow", "flight", "gol"]))
