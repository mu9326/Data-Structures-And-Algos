from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = [[] for _ in range(len(nums) + 1)]

        # print("res: ", res)

        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        # print("count: ", count)

        for key, val in count.items():
            # print("key: ", key)
            # print("val: ", val)
            res[val].append(key)

        # print("res: ", res)

        top_k = []

        for i in range(len(res) - 1, 0, -1):
            # res[i] is a sublist
            for j in res[i]:
                top_k.append(j)
                if len(top_k) == k:
                    return top_k

        return top_k
