"""
Task: 4
URL: https://leetcode.com/problems/product-of-array-except-self/
"""

# O(n) алгоритм без деления

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        # Вычисление префиксных и постфиксных произведений
        prefix_product = [1] * n
        postfix_product = [1] * n

        prefix_product[0] = nums[0]
        postfix_product[0] = nums[n - 1]
        for i in range(1, n):
            prefix_product[i] = prefix_product[i - 1] * nums[i]
            postfix_product[i] = postfix_product[i - 1] * nums[n - i - 1]

        # Вычисляем результат применяя два списка без деления
        result[0] = postfix_product[n - 2]
        for i in range(1, n - 1):
            result[i] = prefix_product[i - 1] * postfix_product[n - i - 2]
        result[n - 1] = prefix_product[n - 2]

        return result
