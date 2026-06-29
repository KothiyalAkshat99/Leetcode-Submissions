"""
Problem Name: Unique Paths
Difficulty: Medium
Tags: Math, Dynamic Programming, Combinatorics
"""

"""
Submission 1
Language: python3
Runtime: 4 ms
Memory: 19.9 MB
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        
        def recur(r, c):
            # Out of bounds
            if r >= m or c >= n:
                return 0
            # If we reach end of board
            if r == m - 1 and c == n - 1:
                return 1
            # If (r, c) in cache
            if (r, c) in memo:
                return memo[(r, c)]

            ret = recur(r + 1, c) + recur(r, c + 1)
            memo[(r, c)] = ret
            return memo[(r, c)]
        
        return recur(0, 0)

