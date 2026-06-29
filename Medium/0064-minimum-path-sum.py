"""
Problem Name: Minimum Path Sum
Difficulty: Medium
Tags: Array, Dynamic Programming, Matrix
"""

"""
Submission 1
Language: python3
Runtime: 25 ms
Memory: 23.1 MB
"""
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dp = [[-1]*COLS for _ in range(ROWS)]

        def recur(r: int, c: int) -> int:
            if r == ROWS or c == COLS:
                return float('inf')
            
            if r == ROWS - 1 and c == COLS - 1:
                return grid[r][c]
            
            if dp[r][c] != -1:
                return dp[r][c]
            
            ret = min(recur(r+1, c), recur(r, c+1))
            dp[r][c] = grid[r][c] + ret

            return dp[r][c]
        
        return recur(0, 0)

