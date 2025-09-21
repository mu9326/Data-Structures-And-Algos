class Solution:
    def validPalindrome(self, s: str) -> bool:
        # write a helper function that checks if the string is a valid palindrome
        def helper(s):
            # initialize the left and right pointers
            left, right = 0, len(s) - 1
            # if any of the characters don't match, return false
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1

            # at the end, return True
            return True

        # initialize the left and right pointers
        left, right = 0, len(s) - 1
        # if there is a mismatch
        while left < right:
            # call the function on the two possible strings
            if s[left] != s[right]:
                if helper(s[left + 1 : right + 1]) or helper(s[left:right]):
                    return True
                else:
                    return False

            left += 1
            right -= 1

        return True


# print(Solution().validPalindrome("abc"))
