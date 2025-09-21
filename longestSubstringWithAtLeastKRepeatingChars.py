class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def getMaxUniqueLetters(s: str) -> int:
            seen = [False] * 26
            max_unique = 0
            for char in s:
                idx = ord(char) - ord("a")
                if not seen[idx]:
                    seen[idx] = True
                    max_unique += 1
            return max_unique

        max_unique = getMaxUniqueLetters(s)
        result = 0
        n = len(s)

        for curr_unique in range(1, max_unique + 1):
            count_map = [0] * 26
            window_start = window_end = unique = count_at_least_k = 0

            while window_end < n:
                if unique <= curr_unique:
                    idx = ord(s[window_end]) - ord("a")

                    if count_map[idx] == 0:
                        unique += 1
                    count_map[idx] += 1

                    if count_map[idx] == k:
                        count_at_least_k += 1
                    window_end += 1

                else:
                    idx = ord(s[window_start]) - ord("a")

                    if count_map[idx] == k:
                        count_at_least_k -= 1
                    count_map[idx] -= 1

                    if count_map[idx] == 0:
                        unique -= 1
                    window_start += 1

                if unique == curr_unique and unique == count_at_least_k:
                    result = max(result, window_end - window_start)

        return result
