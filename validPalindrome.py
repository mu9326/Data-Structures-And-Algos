class Solution:
    def isPalindrome(self, s: str) -> bool:
        # initialize the left and right pointers
        left, right = 0, len(s) - 1

        def isAlphaNum(c):
            if (
                (ord("a") <= ord(c) <= ord("z"))
                or (ord("0") <= ord(c) <= ord("9"))
                or (ord("A") <= ord(c) <= ord("Z"))
            ):
                return True
            return False

        while left <= right:
            print("c", s[left])
            while not isAlphaNum(s[left]) and left < right:
                print("Increasing left for ", s[left])
                left += 1
                print("left ", left)
            while not isAlphaNum(s[right]) and left < right:
                print("Increasing right for ", s[right])
                right -= 1
                print("right ", right)

            print("Comparing ", s[left].lower(), "and", s[right].lower())
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
