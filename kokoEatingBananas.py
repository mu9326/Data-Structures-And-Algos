from typing import List
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # go over the array and find the max value
        l, r = 1, max(piles)

        # initialize the speeds array from 1 to max value
        # initialize minSum
        min_speed = r

        # binary search on speeds -
        # initialize left and right pointers
        while l <= r:
            # while l <= r:
            # find mid
            mid = (l + r) // 2
            # take the mid and divide it by each value in the piles array (the division should be rounded up)
            # and calculate the sum
            time = 0
            for i in piles:
                time += math.ceil(i / mid)
            # if the sum <= h:
            if time <= h:
                min_speed = mid
                # decrease right
                r -= 1
            else:
                l += 1

        return min_speed


print(Solution().minEatingSpeed(piles=[3, 6, 7, 11], h=8))
