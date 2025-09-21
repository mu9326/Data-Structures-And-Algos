class Solution:
    def minNumberOfPrimes(self, n: int, m: int) -> int:
        # write a function to calculate m primes
        # sieve of eratosthenes
        # initialize a primes array until m with default values of 0
        nums = [1 for _ in range(m + 1)]
        primes = []

        # iterate over the primes array (from index 2)
        for i in range(2, len(nums)):
            # if the value is equal to 1:
            if nums[i] == 1:
                # the value is a prime number
                primes.append(i)
                # we iterate once again over the array - taking the product of the prime number
                for j in range(2, len(nums)):
                    # and the value at the array
                    # if the product is less than the len of the primes array:
                    if i * j < len(nums):
                        # we go to the index of the product and update it to 0
                        nums[i * j] = 0

        # print(nums)
        # print(primes)
        # iterate

        # coin change problem
        pass

    def minNumberOfPrimes2(self, n: int, m: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return -1

        primes = []
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, n + 1):
            if sieve[i]:
                primes.append(i)
                if len(primes) == m:
                    break

                for j in range(i * i, n + 1, i):
                    sieve[j] = False

        print(primes)
        dp = [float("inf") for _ in range(n + 1)]
        # print(dp)
        # seed the value for 0
        dp[0] = 0

        # iterate over the dp array:
        for i in range(n + 1):
            # if the value at i is not equal to inf:
            if dp[i] != float("inf"):
                # get the value at this position (minCoins) and add 1 to it
                minPrimes = dp[i] + 1
                # iterate over the coins array
                for j in primes:
                    # if the value at coins[j] + i has a value greater than minCoins
                    # update it to minCoins
                    if i + j < len(dp):
                        dp[i + j] = min(minPrimes, dp[i + j])

        print(dp)
        # return the dp[amount]
        return dp[n]


print(Solution().minNumberOfPrimes2(10, 2))
print(Solution().minNumberOfPrimes2(15, 5))
