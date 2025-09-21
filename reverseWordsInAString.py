class Solution:
    def reverseWords(self, s: str) -> str:
        new_s = " ".join(s.split(" ")[::-1]).strip(" ")

        ret = []

        for i, c in enumerate(new_s):
            if i < len(new_s) - 1 and new_s[i] == new_s[i + 1] == ".":
                i += 1
            else:
                ret.append(c)
                i += 1

        return "".join(ret)
