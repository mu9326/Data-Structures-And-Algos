class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        # iterate over the string
        for i in range(len(s)):
            # assume each char is the center
            # odd length strings
            # if len(s) % 2 != 0:
            # initialize the left and right pointers to i and i
            left, right = i, i

            # while loop -
            # check if the left and right are equal (provided that they are within bounds)
            while left >= 0 and right < len(s) and s[left] == s[right]:
                # update the res and resLen variable if resLen > curr res
                new_res = s[left : right + 1]
                if resLen < len(new_res):
                    res = s[left : right + 1]
                    resLen = len(new_res)
                left -= 1
                right += 1
            # update the pointers
            # else:
            left, right = i, i + 1

            # while loop -
            # check if the left and right are equal (provided that they are within bounds)
            while left >= 0 and right < len(s) and s[left] == s[right]:
                # update the res and resLen variable if resLen > curr res
                new_res = s[left : right + 1]
                if resLen < len(new_res):
                    res = s[left : right + 1]
                    resLen = len(new_res)
                left -= 1
                right += 1
            # for even length strings, just initialize them at 0, i + 1

        # return the res
        return res


print(Solution().longestPalindrome("babaaaaaaaaada"))
print(Solution().longestPalindrome("babad"))
