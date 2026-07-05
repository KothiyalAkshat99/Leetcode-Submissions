"""
Problem Name: Longest Increasing Path in a Matrix
Difficulty: Hard
Tags: Array, Dynamic Programming, Depth-First Search, Breadth-First Search, Graph Theory, Topological Sort, Memoization, Matrix
"""

"""
Submission 1
Language: python3
Runtime: 105 ms
Memory: 21.6 MB
"""
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = [[-1] * COLS for _ in range(ROWS)]

        def recur(r: int, c: int, prev: int) -> int:
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or \
                matrix[r][c] <= prev:
                return 0
            
            if dp[r][c] != -1:
                return dp[r][c]
            
            val = matrix[r][c]

            dp[r][c] = max(
                1 + recur(r - 1, c, val),   # Up
                1 + recur(r + 1, c, val),   # Down
                1 + recur(r, c - 1, val),   # Left
                1 + recur(r, c + 1, val)    # Right
            )

            return dp[r][c]
        
        ret = 0
        for r in range(ROWS):
            for c in range(COLS):
                ret = max(ret, recur(r, c, -1))
        
        return ret

