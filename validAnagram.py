class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_map = {}
        t_map = {}

        for c in s:
            s_map[c] = 1 + s_map.get(c, 0)

        for c in t:
            t_map[c] = 1 + t_map.get(c, 0)

        return s_map == t_map
