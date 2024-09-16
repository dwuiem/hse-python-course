"""
Task: 5
URL: https://leetcode.com/problems/minimum-size-subarray-sum/
"""

# Будем использовать скользящее окно и прибавлять прибавлять/убавлять значения от текущей суммы

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        s = 0
        left = 0
        right = 0
        min_len = len(nums) + 1
        while right < len(nums):
            s += nums[right]
            while s >= target:
                # Обновляем результат
                min_len = min(min_len, right - left + 1)
                s -= nums[left]
                left += 1
            right += 1
        if min_len == len(nums) + 1:
            return 0
        else: 
            return min_len

