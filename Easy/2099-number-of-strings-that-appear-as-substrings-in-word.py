"""
Problem Name: Number of Strings That Appear as Substrings in Word
Difficulty: Easy
Tags: Array, String
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 19.3 MB
"""
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        count = 0
        for pattern in patterns:
            if pattern in word:
                count += 1
        
        return count

