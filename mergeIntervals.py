from typing import List


class Solution:
    # BRUTE FORCE -Time Complexity (O (nlogn + 2n))
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # initialize res
        res = []

        # sort the intervals array
        intervals.sort()

        # iterate over sorted intervals:
        for i in range(len(intervals)):
            # start, end = intervals[i]
            newInterval = intervals[i]

            # skip if already merged inside the last interval in res
            if res and newInterval[1] <= res[-1][1]:
                continue

            # iterate over intervals onwards of i + 1:
            for j in range(i + 1, len(intervals)):
                if intervals[j][0] <= newInterval[1]:
                    end = max(newInterval[1], intervals[j][1])
                else:
                    break

            res.append([newInterval[0], end])
        return res

    # Optimal - Time Complexity (O(nlogn + n))
    def merge2(self, intervals: List[List[int]]) -> List[List[int]]:
        # initialize the res array
        res = []

        # sort the intervals array
        intervals.sort()

        # initialize the initial newInterval
        newInterval = intervals[0]

        # iterate over the sorted array:
        for i in range(len(intervals)):
            # if i is overlapping with the newInterval i.e. intervals[i][0] <= newInterval:
            # if the start of the current interval is lower than the end of the newInterval
            if intervals[i][0] <= newInterval[1]:
                # update the end of the newInterval to the max of the two
                newInterval[1] = max(intervals[i][1], newInterval[1])
            else:
                # append the new interval to the res
                res.append(newInterval)
                # the current interval is the new interval because it is non-overlapping
                newInterval = intervals[i]

        res.append(newInterval)
        return res

    # Optimal, but refined - Time Complexity (O(nlogn + n))
    def merge3(self, intervals: List[List[int]]) -> List[List[int]]:
        # initialize the res array
        res = []

        # sort the intervals array
        intervals.sort()

        # # initialize the initial newInterval
        # newInterval = intervals[0]

        # iterate over the sorted array:
        for i in range(len(intervals)):
            # if i is overlapping with the newInterval i.e. intervals[i][0] <= newInterval:
            if not res or intervals[i][0] > res[-1][1]:
                # update the end of the newInterval to the max of the two
                res.append(intervals[i])
            else:
                res[-1][1] = max(intervals[i][1], res[-1][1])

        return res


print(
    Solution().merge3(
        [[1, 3], [2, 4], [2, 6], [8, 9], [8, 10], [9, 11], [15, 18], [16, 17]]
    )
)
