from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:

        # start the partition from index 0 and end it at 0, 1, 2, 3, .. len(str) (inclusive)

        # backtrack function(start index, end index)
            # check if the word from start idx to end idx is a palindrome
            # if it is:
                # take the next character by itself

                # take str[next:len(str)] 
        pass
