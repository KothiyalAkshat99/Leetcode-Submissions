"""
Problem Name: Count the Number of Special Characters I
Difficulty: Easy
Tags: Hash Table, String
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 19.2 MB
"""
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        hashset = set(word)
        count = 0
        
        for i in range(26):
            lwr = chr(ord('a') + i)
            upr = chr(ord('A') + i)

            if lwr in hashset and upr in hashset:
                count += 1

        return count

