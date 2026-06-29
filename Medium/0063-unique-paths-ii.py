"""
Problem Name: Unique Paths II
Difficulty: Medium
Tags: Array, Dynamic Programming, Matrix
"""

"""
Submission 1
Language: python3
Runtime: 116 ms
Memory: 19.6 MB
"""
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        memo = [[0] * COLS for _ in range(ROWS)]

        def recur(r: int, c: int) -> int:
            # Base Case - OOB or obstacle found
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or obstacleGrid[r][c]:
                return 0
            
            if r == ROWS - 1 and c == COLS - 1:
                return 1
            
            if memo[r][c]:
                return memo[r][c]
            
            memo[r][c] = recur(r + 1, c) + recur(r, c + 1)
            return memo[r][c]
        
        return recur(0, 0)

