from typing import List


class Solution:
    # newInterval could be totally outside of intervals
    # newInterval can be within bounds -
    # 1. overlapping
    # 2. non-overlapping

    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        pass


# len(intervals) == 0? Yes
# len(newInterval) == 0? No
# intervals[i], newInterval be valid? not necessarily
# minimum and maximum values the interval array can take? 0, 10^5
