"""
Problem Name: Detect Cycles in 2D Grid
Difficulty: Medium
Tags: Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix
"""

"""
Submission 1
Language: python3
Runtime: 419 ms
Memory: 121.5 MB
"""
class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        dirs = ((0, -1), (0, 1), (-1, 0), (1, 0))
        
        def dfs(r: int, c: int, pr: int, pc: int):
            visited.add((r, c))

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if (nr, nc) != (pr, pc):
                    if 0 <= nr < ROWS and 0 <= nc < COLS:
                        if grid[nr][nc] == grid[r][c]:
                            if (nr, nc) in visited or dfs(nr, nc, r, c):
                                return True
            
            return False
        
        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) not in visited and dfs(i, j, -1, -1):
                    return True
        
        return False

"""
Submission 2
Language: python3
Runtime: 447 ms
Memory: 145.8 MB
"""
class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        
        def dfs(r: int, c: int, pr: int, pc: int):
            if r < 0 or r == ROWS or c < 0 or c == COLS:
                return False
            
            if pr != -1 and grid[r][c] != grid[pr][pc]:
                return False
            
            if (r, c) in visited:
                return True

            visited.add((r, c))

            ret = (
                ((r + 1, c) != (pr, pc) and dfs(r + 1, c, r, c)) or
                ((r - 1, c) != (pr, pc) and dfs(r - 1, c, r, c)) or
                ((r, c + 1) != (pr, pc) and dfs(r, c + 1, r, c)) or
                ((r, c - 1) != (pr, pc) and dfs(r, c - 1, r, c))
            )
            
            return ret
        
        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) not in visited and dfs(i, j, -1, -1):
                    return True
        
        return False

