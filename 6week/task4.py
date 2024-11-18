'''
URL: https://leetcode.com/problems/longest-substring-without-repeating-characters/
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}
        max_len = 0
        left = 0
        for right in range(0, len(s)):
            if s[right] not in map or map[s[right]] < left:
                map[s[right]] = right
                max_len = max(max_len, right - left + 1)
            else:
                left = map[s[right]] + 1
                map[s[right]] = right
        return max_len