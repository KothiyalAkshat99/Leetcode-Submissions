"""
Problem Name: Total Waviness of Numbers in Range I
Difficulty: Medium
Tags: Math, Dynamic Programming, Enumeration
"""

"""
Submission 1
Language: python3
Runtime: 352 ms
Memory: 19.2 MB
"""
class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        if num1 < 100:
            if num2 < 100:
                return 0
            num1 = 100


        def waviness(n: int) -> int:
            s = str(n)
            wav = 0
            for a, b, c in zip(s, s[1:], s[2:]):
                if (a > b < c) or (a < b > c):
                    wav += 1
            
            return wav


        ret = 0
        
        for n in range(num1, num2 + 1):
            ret += waviness(n)
        
        return ret

