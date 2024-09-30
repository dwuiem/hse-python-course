"""
Task1: Generate Parenthesis
URL: https://leetcode.com/problems/generate-parentheses/
"""

from typing import List


class Solution:
    def generate(self, combinations: list, buffer: str, pairs, opened, closed):
        if opened >= pairs and closed >= pairs:
            combinations.append(buffer)
        # Если открытых скобок нет, то открываем
        elif opened == 0:
            self.generate(combinations, buffer + "(", pairs, opened + 1, closed)

        # Если открытых столько же сколько пар то закрываем
        elif opened == pairs and closed < pairs:
            self.generate(combinations, buffer + ")", pairs, opened, closed + 1)

        # Если краевых случаев нет
        else:
            # Открываем скобочку и продолжаем генерацию
            if opened < pairs:
                self.generate(combinations, buffer + "(", pairs, opened + 1, closed)
            # И генерируем для закрытой скобки (если их меньше чем открытых)
            if closed < opened:
                self.generate(combinations, buffer + ")", pairs, opened, closed + 1)

    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.generate(result, "", n, 0, 0)
        return result
