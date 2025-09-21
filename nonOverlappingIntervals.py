from typing import List


class Solution:
    # [[1,2],[2,3],[3,4],[1,3]]
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort intervals based on the second value in the list (ascending) # [[1, 2], [1, 3], [2, 3], [3, 4]]
        intervals = sorted(intervals, key=lambda x: x[1])
        print(intervals)

        # initialize the endTime variable (initially equal to the endTime of the first interval) # endTime = 4
        endTime = intervals[0][1]

        # initialize a variable count that will store the number of non-overlapping intervals (initially equal to 1) # count = 3
        count = 1

        # we iterate over the sorted array (1, len(intervals)) # [3, 4]
        for i in range(1, len(intervals)):
            # if start time of a particular interval >= current endTime:
            if intervals[i][0] >= endTime:
                # endTime = new endTime
                endTime = intervals[i][1]
                count += 1

        return len(intervals) - count


print(Solution().eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]))
