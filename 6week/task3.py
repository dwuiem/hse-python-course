'''
URL: https://leetcode.com/problems/find-all-anagrams-in-a-string/
'''
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        if len(s) < len(p):
            return result

        p_map = {}
        s_map = {}

        for c in p:
            p_map[c] = p_map.get(c, 0) + 1
        
        for i in range(len(p)):
            s_map[s[i]] = s_map.get(s[i], 0) + 1
        
        if p_map == s_map:
            result.append(0)

        # Sliding window
        for i in range(1, len(s) - len(p) + 1):

            s_map[s[i - 1]] -= 1
            if s_map[s[i - 1]] == 0:
                del s_map[s[i - 1]]

            s_map[s[i + len(p) - 1]] = s_map.get(s[i + len(p) - 1], 0) + 1

            if p_map == s_map:
                result.append(i)

        return result