"""
Task: 2
URL: https://leetcode.com/problems/container-with-most-water/
"""

from types import List

# Решение с использованием двух указателей (жадный алгоритм)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        # Начинаем поиск, расставив указатели по краям, 
        # чтобы длина контейнера изначально была самой большой
        left = 0
        right = len(height) - 1

        while left < right:
            # Определяем столб с минимальной высотой, чтобы найти объём воды
            min_height = min(height[left], height[right])

            # Обновляем максимальный объём
            result = max(result, min_height * (right - left))

            # Сдвигаем столб с минимальной высотой
            if height[left] == min_height:
                left += 1
            else:
                right -= 1
        return result