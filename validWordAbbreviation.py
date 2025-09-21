# A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths. The lengths should not have leading zeros.

# For example, a string such as "substitution" could be abbreviated as (but not limited to):

# "s10n" ("s ubstitutio n")
# "sub4u4" ("sub stit u tion")
# "12" ("substitution")
# "su3i1u2on" ("su bst i t u ti on")
# "substitution" (no substrings replaced)
# The following are not valid abbreviations:

# "s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
# "s010n" (has leading zeros)
# "s0ubstitution" (replaces an empty substring)
# Given a string word and an abbreviation abbr, return whether the string matches the given abbreviation.

# A substring is a contiguous non-empty sequence of characters within a string.

# Example 1:

# Input: word = "internationalization", abbr = "i12iz4n"
# Output: true
# Explanation: The word "internationalization" can be abbreviated as "i12iz4n" ("i nternational iz atio n").
# Example 2:

# Input: word = "apple", abbr = "a2e"
# Output: false
# Explanation: The word "apple" cannot be abbreviated as "a2e".


class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        j = 0
        i = 0
        # iterate over word
        while i < len(word):
            # if i > len(abrr):
            if j >= len(abbr):
                return False
            # if abbr[j] is not a digit and word[i] != abbr[j]:
            if not abbr[j].isdigit() and word[i] != abbr[j]:
                # return false
                return False
            # if abbr[j] is a digit:
            if abbr[j].isdigit():
                # get the number
                num = ""
                while abbr[j].isdigit():
                    num += abbr[j]
                    j += 1

                # increase i to i + num (after casting to int)
                i = i + int(num)
            else:
                j += 1
                i += 1

        if j < len(abbr):
            return False
        return True

    def validWordAbbreviation2(self, word: str, abbr: str) -> bool:
        i = 0  # pointer for word
        j = 0  # pointer for abbr

        while i < len(word) and j < len(abbr):
            if abbr[j].isdigit():
                if abbr[j] == "0":  # leading zero not allowed
                    return False
                num = 0
                while j < len(abbr) and abbr[j].isdigit():
                    num = num * 10 + int(abbr[j])
                    j += 1
                i += num
            else:
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1

        return i == len(word) and j == len(abbr)


# Testing your examples
print(Solution().validWordAbbreviation("internationalization", "i12iz4n"))  # True
print(Solution().validWordAbbreviation("apple", "a2e"))  # False
print(Solution().validWordAbbreviation("substitution", "s10n"))  # True
print(Solution().validWordAbbreviation("apple", "a3e"))  # False


print(Solution().validWordAbbreviation("apple", "a3e"))
