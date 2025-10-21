# Q2. Split Array With Minimum Difference
# Medium
# 4 pt.
# You are given an integer array nums.

# Split the array into exactly two subarrays, left and right, such that left is strictly increasing and right is strictly decreasing.

# Return the minimum possible absolute difference between the sums of left and right. If no valid split exists, return -1.

# A subarray is a contiguous non-empty sequence of elements within an array.

# An array is said to be strictly increasing if each element is strictly greater than its previous one (if exists).

# An array is said to be strictly decreasing if each element is strictly smaller than its previous one (if exists).


from typing import List


class Solution:
    # O(n)
    def splitArray(self, nums: List[int]) -> int:
        # nums = [1, 2, 4, 3]
        # prefix = [1, 3, 7, 10]
        n = len(nums)
        if n == 2:
            return abs(nums[0] - nums[1])

        # prefix sums
        prefix = [0] * n
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + nums[i]

        # left strictly increasing
        # inc = [T, T, T, T]
        inc = [True] * n
        for i in range(1, n):
            if nums[i] <= nums[i - 1]:
                inc[i] = False
            else:
                inc[i] = inc[i - 1]

        # right strictly decreasing
        # dec = [T, T, T, T]
        dec = [True] * n
        for i in range(n - 2, -1, -1):
            if nums[i] <= nums[i + 1]:
                dec[i] = False
            else:
                dec[i] = dec[i + 1]

        # check splits
        min_diff = float("inf")
        valid = False
        for i in range(1, n):
            if inc[i - 1] and dec[i]:
                left_sum = prefix[i - 1]
                right_sum = prefix[n - 1] - prefix[i - 1]
                diff = abs(left_sum - right_sum)
                min_diff = min(min_diff, diff)
                valid = True

        return min_diff if valid else -1

    # Brute Force
    def splitArray2(self, nums: List[int]) -> int:
        if len(nums) == 2:
            return abs(nums[0] - nums[1])

        # [1, 2, 4, 3]

        min_sum = float("inf")
        valid = False

        # iterate over the array (i = 1, 2)
        for i in range(1, len(nums)):
            left = nums[0:i]
            # left = [1]
            # calculate left_sum
            # iterate over left:
            is_left_inc = all(left[j] > left[j - 1] for j in range(1, len(left)))

            right = nums[i:]
            is_right_dec = all(right[j] < right[j - 1] for j in range(1, len(right)))

            if is_left_inc and is_right_dec:
                left_sum = 0
                for l in range(len(left)):
                    # left_sum += element
                    left_sum += left[l]
                right_sum = 0
                for r in range(len(right)):
                    right_sum += right[r]
                # calculate abs(left-right) sums
                diff = abs(left_sum - right_sum)
                # update the minimum sum
                min_sum = min(diff, min_sum)
                valid = True

        # return min_sum if valid else -1
        return min_sum if valid else -1
