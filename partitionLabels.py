from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        size = 0
        end = 0
        res = []

        # first pass
        # populate the hashmap with char : lastIndex
        last_index = {}
        for i, c in enumerate(s):
            last_index[c] = i

        # second pass
        # iterate over the string:
        for i in range(len(s)):
            # check the lastIdex of current char
            if last_index[s[i]] > end:
                # if it is greater than the end, update the end
                end = last_index[s[i]]

            # update the size
            size += 1

            if i == end:
                # append size to result
                res.append(size)
                # reset the size

                size = 0
        return res
