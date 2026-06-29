"""
Problem Name: Maximum Path Score in a Grid
Difficulty: Medium
Tags: Array, Dynamic Programming, Matrix
"""

"""
Submission 1
Language: python3
Runtime: 7373 ms
Memory: 37.4 MB
"""
class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        INF = float("-inf")
        dp = [[[INF] * (k + 1) for _ in range(COLS)] for _ in range(ROWS)]
        
        dp[0][0][0] = 0

        for i in range(ROWS):
            for j in range(COLS):
                for c in range(k + 1):
                    if dp[i][j][c] == INF:
                        continue
                    
                    if i + 1 < ROWS:
                        val = grid[i + 1][j]
                        cost = 0 if val == 0 else 1
                        if c + cost <= k:
                            dp[i + 1][j][c + cost] = max(
                                dp[i + 1][j][c + cost], dp[i][j][c] + val
                            )
                    
                    if j + 1 < COLS:
                        val = grid[i][j + 1]
                        cost = 0 if val == 0 else 1
                        if c + cost <= k:
                            dp[i][j + 1][c + cost] = max(
                                dp[i][j + 1][c + cost], dp[i][j][c] + val
                            )
        
        ret = max(dp[ROWS - 1][COLS - 1])
        return -1 if ret < 0 else ret

