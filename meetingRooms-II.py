from collections import defaultdict
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # [[0, 10], [5, 15], [5, 30]]

        # initialize and fill-in the start and end times array
        start_times, end_times = (
            [0 for _ in range(len(intervals))],
            [0 for _ in range(len(intervals))],
        )
        for i in range(len(intervals)):
            start_times[i] = intervals[i][0]
            end_times[i] = intervals[i][1]

        # sort the start times array # []
        start_times.sort()
        # sort the end times array
        end_times.sort()

        # start_times = [0, 4, 5, 5, 6, 7, 8, 9, 10]
        # end_times =   [2, 5, 6, 7, 8, , 9, 10, 11]

        # initialize a pointer at the start array and a pointer at the end array
        # initialize a count variable (initially 0) and a maxCount variable
        # start = 3, end  = 1, count = 2, maxC = 2
        start, end, count, maxCount = 0, 0, 0, 0

        # while start pointer is less than len(start array):
        while start < len(start_times):
            # if the value at start pointer is lower than the value at the end pointer
            if start_times[start] < end_times[end]:
                # we move the start pointer by 1
                start += 1
                # increase count
                count += 1
                # update maxCount if needed
                maxCount = max(maxCount, count)
            else:
                # we move the end pointer by 1
                end += 1
                # we decrement the count
                count -= 1

        return maxCount

    # Sweeping Line Algorithm
    def minMeetingRooms2(self, intervals: List[List[int]]) -> int:
        mp = defaultdict(int)
        for i in intervals:
            mp[i[0]] += 1
            mp[i[1]] -= 1

        print(mp)
        prev = 0
        res = 0
        for i in sorted(mp.keys()):
            prev += mp[i]
            res = max(res, prev)
        return res


print(
    Solution().minMeetingRooms(
        [[0, 2], [4, 5], [5, 6], [5, 7], [6, 8], [7, 9], [8, 9], [9, 10], [10, 11]]
    )
)

print(Solution().minMeetingRooms2([[0, 10], [5, 15], [15, 30]]))
