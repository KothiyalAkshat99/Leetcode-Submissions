"""
Problem Name: Concatenate Non-Zero Digits and Multiply by Sum I
Difficulty: Easy
Tags: Math
"""

"""
Submission 1
Language: python3
Runtime: 1 ms
Memory: 19.4 MB
"""
class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = ""
        sum_digits = 0

        for digit in str(n):
            if digit != '0':
                x += digit
                sum_digits += int(digit)

        return int(x) * sum_digits if sum_digits else 0

