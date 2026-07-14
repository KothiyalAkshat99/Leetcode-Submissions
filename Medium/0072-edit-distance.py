"""
Problem Name: Edit Distance
Difficulty: Medium
Tags: String, Dynamic Programming
"""

"""
Submission 1
Language: python3
Runtime: 41 ms
Memory: 24.3 MB
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1 and not word2:
            return 0
        
        memo = {}
        
        def recur(idx1: int, idx2: int) -> int:
            # Base Case - end of both words reached
            if idx1 == len(word1) and idx2 == len(word2):
                return 0
            # When only one word ends, #ops = remaining length of other word
            if idx1 == len(word1):
                return len(word2) - idx2
            if idx2 == len(word2):
                return len(word1) - idx1
            
            # Solution in Cache
            if (idx1, idx2) in memo:
                return memo[(idx1, idx2)]
            
            if word1[idx1] == word2[idx2]:
                ret = recur(idx1 + 1, idx2 + 1)
            else:
                insert = 1 + recur(idx1, idx2 + 1)
                delete = 1 + recur(idx1 + 1, idx2)
                replace = 1 + recur(idx1 + 1, idx2 + 1)
                ret = min(insert, delete, replace)
            
            memo[(idx1, idx2)] = ret
            return ret
        
        return recur(0, 0)

"""
Submission 2
Language: python3
Runtime: 44 ms
Memory: 22.6 MB
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1 and not word2:
            return 0

        len1 = len(word1)
        len2 = len(word2)
        dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

        for idx1 in range(len1 + 1):
            dp[idx1][0] = idx1
        
        for idx2 in range(len2 + 1):
            dp[0][idx2] = idx2
        
        for idx1 in range(1, len1 + 1):
            for idx2 in range(1, len2 + 1):
                if word1[idx1 - 1] == word2[idx2 - 1]:
                    dp[idx1][idx2] = dp[idx1 - 1][idx2 - 1]
                else:
                    dp[idx1][idx2] = 1 + min(dp[idx1- 1][idx2], dp[idx1][idx2 - 1], dp[idx1 - 1][idx2 - 1])
        
        return dp[-1][-1]

