"""
Problem Name: Modify the Matrix
Difficulty: Easy
Tags: Array, Matrix
"""

"""
Submission 1
Language: python3
Runtime: 3 ms
Memory: 19.3 MB
"""
class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(matrix), len(matrix[0])

        for c in range(COLS):
            max_val = matrix[0][c]

            for r in range(ROWS):
                max_val = max(max_val, matrix[r][c])
            
            for r in range(ROWS):
                if matrix[r][c] == -1:
                    matrix[r][c] = max_val
        
        return matrix

