"""
Task: 4
URL: https://leetcode.com/problems/jump-game/
"""

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        target = n - 1

        for i in range(n - 1, -1, -1):
            if target <= i + nums[i]:
                target = i

        return target == 0
