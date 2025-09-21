from typing import List
import math
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        # for each point in the points array, get the distance and store it in a different array
        for point in points:
            x = point[0]
            y = point[1]

            distance = (math.pow(x, 2) - 0) + (math.pow(y, 2) - 0)
            distances.append([distance, x, y])
            print("distances: ", distances)

        # heapify this new array
        heapq.heapify(distances)
        print("Heapified array: ", distances)

        # initialize a counter and a res array
        counter, res = 0, []

        # while counter != k:
        while counter != k:
            # pop the point from the heap and add it to the res array
            point = heapq.heappop(distances)
            res.append([point[1], point[2]])
            counter += 1

        # return the res
        return res


object = Solution()
print(object.kClosest([[3, 3], [5, -1], [-2, 4]], 2))
