from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # nums1 = [1, 3, 4, 7, 10, 12]
        # nums2 = [2, 3, | 6, 15]

        # formula to determine the number of elements needed for the left half
        left_half = (len(nums1) + len(nums2) + 1) // 2  # 10/2 = 5

        # select the array that is shorter in length and our search space is its length
        # assign left and right pointers at 0 and len - 1
        left = 0  # left = 0
        if len(nums1) < len(nums2):
            arr = nums1
            other_arr = nums2
        else:
            arr = nums2
            other_arr = nums1
        right = len(arr)

        # calculate the mid (this is l1) (if it's out of bounds, l1 will be negative inf)
        while left <= right:
            # mid + 1 is r1 (if it's out of bounds, l1 will be positive inf)
            mid = (left + right) // 2  # mid = 3 - 0 // 2 = 3 // 2 = 1
            # we select 2 elements from nums2, we need 3 more

            l1 = arr[mid - 1] if mid > 0 else float("-inf")
            r1 = arr[mid] if mid < len(arr) else float("inf")

            cut2 = left_half - mid
            l2 = other_arr[cut2 - 1] if cut2 > 0 else float("-inf")
            r2 = other_arr[cut2] if cut2 < len(other_arr) else float("inf")

            if l1 > r2:
                right = mid - 1
            elif l2 > r1:
                left = mid + 1
            else:
                # correct partition found
                if (len(nums1) + len(nums2)) % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2
                else:
                    return max(l1, l2)
