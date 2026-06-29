"""
Problem Name: Maximum Number of Balloons
Difficulty: Easy
Tags: Hash Table, String, Counting
"""

"""
Submission 1
Language: python3
Runtime: 3 ms
Memory: 19.2 MB
"""
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        char_map = Counter(text)
        balloon = Counter('balloon')
        ret_count = len(text)
        
        for char in balloon:
            ret_count = min(ret_count, char_map[char] // balloon[char])
        
        return ret_count

