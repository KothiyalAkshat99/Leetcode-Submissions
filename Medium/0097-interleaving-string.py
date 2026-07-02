"""
Problem Name: Interleaving String
Difficulty: Medium
Tags: String, Dynamic Programming
"""

"""
Submission 1
Language: python3
Runtime: 49 ms
Memory: 20.1 MB
"""
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        memo = {}
        
        def recur(i: int, j: int) -> bool:      # s1_index, s2_index
            if i == len(s1) and j == len(s2):
                return True
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            # Choice A: Can we take a character from s1
            if i < len(s1) and s1[i] == s3[i + j]:
                if recur(i + 1, j):
                    return True
            
            # Choice B: Can we take a character from s2
            if j < len(s2) and s2[j] == s3[i + j]:
                if recur(i, j + 1):
                    return True
            
            memo[(i, j)] = False
            return memo[(i, j)]
        
        return recur(0, 0)

