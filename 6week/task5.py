'''
URL: https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/
'''

from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        result = 0
        if len(nums) <= 1:
            return result
        
        left = 0
        target_null = 0

        # Найти первый ноль
        while target_null < len(nums) and nums[target_null] != 0:
            target_null += 1
        
        if target_null == len(nums):
            return len(nums) - 1
        
        right = target_null + 1
        if right < len(nums) and nums[right] == 1:
            counter = right - left + 1
        else:
            result = target_null - left + 1
            left = target_null + 1
            target_null = right
            counter = 1
            right += 1
        
        while right < len(nums):
            if nums[right] == 0:
                result = max(result, counter)
                left = target_null + 1
                target_null = right
            counter = right - left + 1
            right += 1
        
        result = max(result, counter)
        return result - 1