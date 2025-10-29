from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # [[3, 4, 5], [4, 5, 6]]
        # target = [3, 2, 5]

        # temp = []
        validated = [False, False, False]

        # triplet = [4, 5, 6]
        # go over each triplet in the list:
        for triplet in triplets:
            # if either of the values in the triplet is greater than the corresponding val in target
            if (
                triplet[0] > target[0]
                or triplet[1] > target[1]
                or triplet[2] > target[2]
            ):
                continue
            # if the first value of the triplet is the same as the first value of the target:
            if triplet[0] == target[0]:
                # change first True to validated
                validated[0] = True
            # do the same for the other two values
            if triplet[1] == target[1]:
                # change first True to validated
                validated[1] = True
            if triplet[2] == target[2]:
                # change first True to validated
                validated[2] = True

        # check if all values in validated are True:
        return validated[0] and validated[1] and validated[2]
