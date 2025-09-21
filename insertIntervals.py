from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        res = []

        i = 0

        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        # NOTE: Be careful of this condition, it has to be less than OR equal (instead of just less than) -> intervals[i][0] <= newInterval[1]
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        res.append(newInterval)

        while i < len(intervals):
            res.append(intervals[i])
            i += 1

        return res


print(Solution().insert([[1, 2], [3, 4], [5, 7], [8, 10], [12, 16]], [6, 8]))

print(Solution().insert([[1, 2], [3, 4], [5, 7], [8, 10], [12, 16]], [0, 8]))
