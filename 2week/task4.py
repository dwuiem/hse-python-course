"""
Task 4
URL: https://leetcode.com/problems/string-compression/
"""

# Two pointers solve


class Solution:
    def compress(self, chars: List[str]) -> int:
        left = 0
        right = 0

        while left < len(chars) and right < len(chars):
            chars[left] = chars[right]
            counter = 0

            while right < len(chars) and chars[left] == chars[right]:
                right += 1
                counter += 1

            if counter == 1:
                left += 1
                continue

            for num in str(counter):
                left += 1
                chars[left] = num

            left += 1

        return left
