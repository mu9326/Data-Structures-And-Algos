from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # initialize prefix_product and suffix_product --> both equal to 1 # prefix, suffix = 1
        prefix, suffix = 1, 1
        # initialize the output array # res = [4, 2] nums = # [2, 4]
        res = [1]

        # 1. iterate over the nums array (except the last element)-
        for i in range(len(nums) - 1):
            # update prefix = prefix * curr_ele # 1 * 2
            prefix = prefix * nums[i]
            # append the element at position (curr + 1)
            res.append(prefix)

        print(res)
        # 2. iterate over the nums array (backwards until the 0th element)
        for j in range(len(nums) - 1, -1, -1):
            # prev_suffix = suffix # 4
            prev_suffix = suffix
            # update suffix = suffix * curr[nums] # 4 * 2 = 8
            suffix = suffix * nums[j]
            # if it's the last element, we continue
            if j == (len(nums) - 1):
                continue
            else:
                # change the ele at the res element to prev_suffix * ele # 1 * 4 = 4
                new_res = res[j] * prev_suffix
                res[j] = new_res
        return res
