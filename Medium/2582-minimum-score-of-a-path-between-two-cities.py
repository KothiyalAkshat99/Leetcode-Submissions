"""
Problem Name: Minimum Score of a Path Between Two Cities
Difficulty: Medium
Tags: Depth-First Search, Breadth-First Search, Union-Find, Graph Theory
"""

"""
Submission 1
Language: python3
Runtime: 184 ms
Memory: 75 MB
"""
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)

        for u, v, d in roads:
            adj[u].append((v, d))
            adj[v].append((u, d))
        
        visited = set()
        dq = deque([1])

        ret = float('inf')

        while dq:
            u = dq.popleft()

            for v, d in adj[u]:
                ret = min(ret, d)

                if v not in visited:
                    visited.add(v)
                    dq.append(v)
        
        return ret

"""
Submission 2
Language: python3
Runtime: 171 ms
Memory: 101.7 MB
"""
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)

        for u, v, d in roads:
            adj[u].append((v, d))
            adj[v].append((u, d))
        
        visited = set()
        ret = float('inf')
        
        def dfs(node) -> None:
            visited.add(node)
            
            nonlocal ret
            for nb, wt in adj[node]:
                ret = min(ret, wt)
                if nb not in visited:
                    dfs(nb)
        
        dfs(1)
        return ret

