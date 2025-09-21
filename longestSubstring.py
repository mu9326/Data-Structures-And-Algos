# Notes:
# Make notes on the approach (remember, we can use a for loop as well)
# set operations - remember there is a remove operation
# memorize the windowLen formula
# do you want to make notes on the map approach? (the optimal version in Neetcode)


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # "abcabcbb"

        # initialize left and right pointers
        left, right = 0, 0

        # initialize the lenOfSubstring variable and the set
        longest = 0  # 3
        duplicates = set()  # {b}

        # while right < len(s):
        while right < len(s):
            # check if the window is valid
            # while it is not valid (i.e. s[r] cannot be added successfully to the set)
            while s[right] in duplicates:
                # remove s[left]
                duplicates.remove(s[left])
                # update left
                left += 1

            # if it is valid
            # add s[right] to the set
            duplicates.add(s[right])
            # get windowLen and update the longest
            windowLen = (right - left) + 1
            longest = max(windowLen, longest)
            # increase right
            right += 1

        return longest

        # edge cases -
        # 1. can s be empty?
        # 2. length of s is 1
