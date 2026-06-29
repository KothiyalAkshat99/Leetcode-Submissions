"""
Problem Name: Count the Number of Special Characters II
Difficulty: Medium
Tags: Hash Table, String
"""

"""
Submission 1
Language: python3
Runtime: 214 ms
Memory: 21.4 MB
"""
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        # Record first occurence of Uppercase
        # Record last occurence of Lowercase
        # If both exist and last_occ_lower < first_occ_upper, count += 1

        last_lower = {}
        first_upper = {}

        for i, char in enumerate(word):
            if char.islower():
                last_lower[char] = i
            else:
                if char not in first_upper:
                    first_upper[char] = i
        
        count = 0

        for char in string.ascii_lowercase:
            if char in last_lower and \
                char.upper() in first_upper and \
                last_lower[char] < first_upper[char.upper()]:
                count += 1
        
        return count

