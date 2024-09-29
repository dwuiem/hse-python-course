"""
Task 5
URL: https://leetcode.com/problems/permutation-in-string/
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        p_map = {}
        s_map = {}

        for c in s1:
            p_map[c] = p_map.get(c, 0) + 1

        for i in range(len(s1)):
            s_map[s2[i]] = s_map.get(s2[i], 0) + 1

        if p_map == s_map:
            return True

        for i in range(1, len(s2) - len(s1) + 1):

            s_map[s2[i - 1]] -= 1
            if s_map[s2[i - 1]] == 0:
                del s_map[s2[i - 1]]

            s_map[s2[i + len(s1) - 1]] = s_map.get(s2[i + len(s1) - 1], 0) + 1

            if p_map == s_map:
                return True

        return False
