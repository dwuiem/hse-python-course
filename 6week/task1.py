'''
URL: https://leetcode.com/problems/find-k-closest-elements/
'''

from bisect import bisect_left
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if k >= len(arr):
            return arr

        closest_idx = bisect_left(arr, x)
        left, right = closest_idx - 1, closest_idx
        result = []

        while left >= 0 and right < len(arr) and len(result) < k:
            if abs(arr[left] - x) <= abs(arr[right] - x):
                result.append(arr[left])
                left -= 1
            else:
                result.append(arr[right])
                right += 1

        while len(result) < k and left >= 0:
            result.append(arr[left])
            left -= 1

        while len(result) < k and right < len(arr):
            result.append(arr[right])
            right += 1

        return sorted(result)