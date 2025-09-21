from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # nums = [100,4,200,1,3,2]
        # add the elements of the list into the set
        nums_set = set()
        for num in nums:
            nums_set.add(num)

        # initialize the longest variable
        longest = 0

        # iterate over nums: #
        for i in range(len(nums)):
            # check if the num is the beginning of a sequence
            # 1. check if the left num is in the set -- T
            if nums[i] - 1 not in nums_set:
                # if it is not, this is the beginning of a sequence
                # update curr_longest = 1
                curr_longest = 1
                # keep checking if the consecutive elements to the right are in the seq # 4?
                while nums[i] + 1 in nums_set:
                    # if it is, update the curr_longest # 4
                    curr_longest += 1
                    nums[i] += 1
                # update the longest to be the max of longest and curr_longest # longest = 4
                longest = max(longest, curr_longest)

        return longest


print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))
