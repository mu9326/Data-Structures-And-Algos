from collections import defaultdict
from typing import List


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_freq = defaultdict(int)
        pair_freq = defaultdict(int)

        num_tuples = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                product = nums[i] * nums[j]
                pair_freq[product] += product_freq[product]
                product_freq[product] += 1

        for count in pair_freq.values():
            num_tuples += 8 * count

        return num_tuples
