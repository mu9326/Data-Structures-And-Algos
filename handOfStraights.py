from typing import List
from collections import heapq


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # check if hand is divisible by groupSize
        if len(hand) % groupSize:
            return False

        count = {}

        # populate the hashmap
        for i in hand:
            count[i] = 1 + count.get(i, 0)

        # initialize the heap
        minHeap = list(count.keys())
        heapq.heapify(minHeap)

        # while the heap is not empty:
        while minHeap:
            top = minHeap[0]

            # iterate range over (top element to top + grpSize):
            for i in range(top, top + groupSize):
                # if i is not in the hashmap, return False
                if i not in count:
                    return False

                # else: decrease the count in the hashmap
                count[i] -= 1
                # if the count is now zero:
                if count[i] == 0:
                    # the top element of the heap HAS to be equal to the current element i.e. i
                    # if it is not, this means that the top element of the heap is lower than i and that i
                    # is the middle element of a potential group which does not exist, so we can return False right here
                    if i != minHeap[0]:
                        return False
                    heapq.heappop(minHeap)

        # return True after the completed iteration is over
        return True
