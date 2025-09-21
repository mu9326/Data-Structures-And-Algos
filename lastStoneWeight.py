from typing import List
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # multiply the values in stones by -1
        for i in range(len(stones)):
            stones[i] = -1 * stones[i]

        # heapify this new list
        heapq.heapify(stones)
        print("stones as max heap: ", stones)

        while len(stones) > 1:
            # get the topmost element using heappop - two times (x and y)
            y = heapq.heappop(stones)  # -4
            x = heapq.heappop(stones)  # -2
            print("popped", x, y)

            # if - x < - y:
            if x < y:  # -1 < -1
                diff = y - x
                print("(x, y, diff): ", x, y, diff)
                # get the diff and push it onto the heap
                heapq.heappush(stones, diff)
            if x == y:
                continue

            print("Length of stones: ", len(stones))

            # if len(stones) == 1:
        if len(stones) == 1:
            return stones[0]

        return 0
