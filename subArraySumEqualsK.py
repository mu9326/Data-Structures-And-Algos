from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # initialize the hashmap with 0 : 1 added
        prefix_lookup = {0: 1}

        # initialize prefix_sum and count
        prefix_sum, count = 0, 0

        # iterate over nums
        for i in range(len(nums)):
            # increase the prefix_sum by the value at i
            prefix_sum += nums[i]

            rem = prefix_sum - k
            # if rem > 0 and rem in hashmap:
            if rem in prefix_lookup:
                # we add this becaue we know that there are hashmap[rem] number of subarrays that have the prefix_sum we are looking for, so we can pick
                # either of them -- hence, we add both to the total count
                count += prefix_lookup[rem]

            # update our hashmap with the current prefix_sum
            prefix_lookup[prefix_sum] = 1 + prefix_lookup.get(prefix_sum, 0)
            print(prefix_lookup)

        return count


print(Solution().subarraySum([-1, -1, 1], 0))
