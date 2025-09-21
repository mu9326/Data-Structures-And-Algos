import math


class Solution:
    # Brute force (O(n))
    def arrangeCoins(self, n: int) -> int:
        coins = n
        for i in range(1, n + 1):
            if i > coins:
                return i - 1
            coins -= i

        return i

    # Binary Search O(logn)
    def arrangeCoins2(self, n: int) -> int:
        def getCoinsNeeded(m):
            return math.floor(((m / 2) * (m + 1)))

        # initialize the left and right pointers
        left, right = 1, n

        while left <= right:
            # calculate mid
            mid = (left + right) // 2
            # coins_needed = apply the formula on the value of the mid
            coins_needed = getCoinsNeeded(mid)
            if coins_needed == n:
                return mid
            if n > coins_needed:
                # update left
                left = mid + 1
            # else:
            else:
                # update right
                right = mid - 1

        return right


print(Solution().arrangeCoins2(8))
print(Solution().arrangeCoins2(5))
