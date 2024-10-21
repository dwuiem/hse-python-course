from typing import List


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:

        x = numerator
        y = denominator

        if x == 0:
            return "0"
        if y == 0:
            return ""
        if y == 1:
            return str(x)

        result = ""
        if (x < 0) ^ (y < 0):
            result += "-"

        x = abs(x)
        y = abs(y)

        result += str(x // y)
        remainder = x % y
        if remainder == 0:
            return result
        result += "."

        remainder_position = {}

        while remainder != 0 and remainder not in remainder_position:
            remainder_position[remainder] = len(result)
            remainder *= 10
            result += str(remainder // y)
            remainder %= y
        if remainder in remainder_position:
            result = (
                result[: remainder_position[remainder]]
                + "("
                + result[remainder_position[remainder] :]
                + ")"
            )

        return result
