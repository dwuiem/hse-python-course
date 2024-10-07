"""
Task: 1
URL: https://leetcode.com/problems/container-with-most-water/
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        left = 0
        right = len(height) - 1

        while left < right:
            min_height = min(height[left], height[right])

            result = max(result, min_height * (right - left))

            if height[left] == min_height:
                left += 1
            else:
                right -= 1
        return result
