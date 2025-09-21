import heapq


class MedianFinder:
    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:  # [3, 2, 7, 4]
        # Add the element
        heapq.heappush(self.small, -1 * num)

        # small = [2]
        # large = [3, 7]

        # if the max value in small is greater than the min value in large (if the values exist) --> while loop
        if self.large and self.small and -self.small[0] > self.large[0]:
            # pop from small
            element = heapq.heappop(self.small)
            # push to large
            heapq.heappush(self.large, -element)

        # Check if two conditions are satisfied -
        # 1. if diff between lengths is more than 1: --> while loop
        if abs(len(self.small) - len(self.large)) > 1:
            # pop the top element from the heap with the higher number of elements (if the value exists)
            # push it into the heap with the lower number of elements
            if len(self.small) > len(self.large):
                element = heapq.heappop(self.small)
                heapq.heappush(self.large, -element)
            else:
                element = heapq.heappop(self.large)
                heapq.heappush(self.small, -1 * element)

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            mid1 = -self.small[0]
            mid2 = self.large[0]
            return (mid1 + mid2) / 2
        elif len(self.small) > len(self.large):
            return -self.small[0]
        else:
            return self.large[0]
