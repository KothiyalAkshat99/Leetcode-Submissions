"""
Problem Name: Process String with Special Operations I
Difficulty: Medium
Tags: String, Simulation
"""

"""
Submission 1
Language: python3
Runtime: 45 ms
Memory: 28.3 MB
"""
class Solution:
    def processStr(self, s: str) -> str:
        result = []

        for char in s:
            if 97 <= ord(char) <= 122:
                result.append(char)
            elif char == '*':
                if result:
                    result.pop()
            elif char == '#':
                result = result + result
            elif char == '%':
                result = result[::-1]
        
        return ''.join(result)

