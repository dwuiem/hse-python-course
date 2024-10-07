"""
Task: 3
URL: https://leetcode.com/problems/insert-interval/
"""

from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        result = []
        ptr = 0

        while ptr < len(intervals) and intervals[ptr][1] < newInterval[0]:
            result.append(intervals[ptr])
            ptr += 1

        if ptr == len(intervals):
            result.append(newInterval)
            return result

        start = min(intervals[ptr][0], newInterval[0])

        while ptr < len(intervals) and intervals[ptr][0] <= newInterval[1]:
            ptr += 1

        if ptr > 0:
            end = max(intervals[ptr - 1][1], newInterval[1])
        else:
            end = newInterval[1]

        result.append([start, end])

        while ptr < len(intervals):
            result.append(intervals[ptr])
            ptr += 1

        return result
