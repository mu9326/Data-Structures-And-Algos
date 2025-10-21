from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1

        total = 0
        start = 0

        # gas = [3, 1, 1], cost = [1, 2, 2]
        for i in range(len(gas)):
            total += gas[i] - cost[i]  # 2
            print(total)
            if total < 0:
                total = 0
                start = i + 1  # 3

        return start


print(Solution().canCompleteCircuit([3, 1, 1], [1, 2, 2]))
