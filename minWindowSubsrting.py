class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # initialize the s and t hashmaps and the need and have variables
        s_map, t_map = {}, {}

        for c in t:
            t_map[c] = 1 + t_map.get(c, 0)
            s_map[c] = 0

        need, have = len(t_map), 0
        # print(need)

        # start the window with left and right at 0
        left, right = 0, 0
        # initialize the res variable
        res = ""

        while right < len(s):
            # if the char at right is in the s hashmap:
            if s[right] in s_map:
                # update its count
                s_map[s[right]] += 1
                # if the updated count is equal to its count in the t-map:
                if s_map[s[right]] == t_map[s[right]]:
                    # update the have variable
                    have += 1

                # while the window is still valid (i.e. need == have):
                while need == have:
                    # calculate the window length
                    windowLen = right - left + 1
                    # update the res variable
                    if res == "" or len(res) > windowLen:
                        res = s[left : right + 1]
                    # check if the value at left is in the s-map
                    if s[left] in s_map:
                        # if it is:
                        # update its count
                        s_map[s[left]] -= 1
                        # if the updated count is less than its count in the t-map:
                        if s_map[s[left]] < t_map[s[left]]:
                            # update the have variable
                            have -= 1
                    # decrease left
                    left += 1

            right += 1

        return res


print(Solution().minWindow("ADOBECODEBANC", "ABC"))
