'''
URL: https://leetcode.com/problems/permutation-in-string
'''

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
    
        # Частоты символов в s1
        s1_freq = [0] * 26
        # Частоты символов для текущего окна в s2
        window_freq = [0] * 26
        
        # Функция для преобразования символа в индекс
        def char_to_index(char):
            return ord(char) - ord('a')
        
        # Заполнение частот для s1 и первого окна s2
        for i in range(len(s1)):
            s1_freq[char_to_index(s1[i])] += 1
            window_freq[char_to_index(s2[i])] += 1
        
        # Проверяем частоты на первом окне
        if s1_freq == window_freq:
            return True
        
        # Скользящее окно
        for i in range(len(s1), len(s2)):
            # Удаляем символ, который выходит из окна
            start_char_index = char_to_index(s2[i - len(s1)])
            window_freq[start_char_index] -= 1
            
            # Добавляем символ, который входит в окно
            end_char_index = char_to_index(s2[i])
            window_freq[end_char_index] += 1
            
            # Проверяем частоты
            if s1_freq == window_freq:
                return True
        
        return False