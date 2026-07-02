"""
Problem Name: Find a Safe Walk Through a Grid
Difficulty: Medium
Tags: Array, Breadth-First Search, Graph Theory, Heap (Priority Queue), Matrix, Shortest Path
"""

"""
Submission 1
Language: python3
Runtime: 39 ms
Memory: 19.5 MB
"""
class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        # 0-1 BFS 
        # Dijkstra but better
        # While traversing edge with wt 0, push to front
        # For wt 1, push to back
        # Smaller distance cells are processed first
        # And each queue op takes O(1) time

        ROWS, COLS = len(grid), len(grid[0])
        dist = [[float('inf')] * COLS for _ in range(ROWS)]
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        dq = deque()
        dq.appendleft((0, 0))
        dist[0][0] = grid[0][0]

        while dq:
            r, c = dq.popleft()
            if r == ROWS - 1 and c == COLS - 1:
                return True
            
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS:
                    continue
                
                cost = dist[r][c] + grid[nr][nc]
                if cost >= health:
                    continue
                
                if cost < dist[nr][nc]:
                    dist[nr][nc] = cost
                    if grid[nr][nc] == 0:
                        dq.appendleft((nr, nc))
                    else:
                        dq.append((nr, nc))
        
        return False

