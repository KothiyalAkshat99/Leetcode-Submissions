"""
Problem Name: Find the Encrypted String
Difficulty: Easy
Tags: String
"""

"""
Submission 1
Language: python3
Runtime: 2 ms
Memory: 19.4 MB
"""
class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        n = len(s)
        ret = [''] * n

        k %= n

        for i in range(n):
            encr_char = s[(i + k) % n]
            ret[i] = encr_char
        
        return ''.join(ret)

