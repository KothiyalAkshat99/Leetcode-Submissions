"""
Problem Name: Longest Common Subsequence
Difficulty: Medium
Tags: String, Dynamic Programming
"""

"""
Submission 1
Language: python3
Runtime: 337 ms
Memory: 44.2 MB
"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1 = len(text1)
        len2 = len(text2)
        dp = [[0]*(len2 + 1) for _ in range(len1 + 1)]
        
        for i in range(len1):
            for j in range(len2):
                if text1[i] == text2[j]:
                    dp[i + 1][j + 1] = 1 + dp[i][j]
                else:
                    dp[i + 1][j + 1] = max(
                        dp[i + 1][j], dp[i][j + 1]
                    )

        return dp[len1][len2]

