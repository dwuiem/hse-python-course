"""
Task: 3
URL: https://leetcode.com/problems/group-anagrams/
"""

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Словарь нужен чтобы определять анаграмы по отсортированному варианту
        m = dict()
        result = []

        # Добавляем слова в словарь
        for s in strs:
            # Определяем ключ как отсортированную анаграму
            key = "".join(sorted(s))

            # Добавляем в нужную группу строку
            if key not in m:
                m[key] = []
            m[key].append(s)

        # Копируем в результат
        for value in m.values():
            anagrams = []
            for s in value:
                anagrams.append(s)
            result.append(anagrams)

        return result
