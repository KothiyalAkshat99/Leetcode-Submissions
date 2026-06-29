"""
Problem Name: Number of Ways to Assign Edge Weights I
Difficulty: Medium
Tags: Math, Tree, Depth-First Search
"""

"""
Submission 1
Language: python3
Runtime: 366 ms
Memory: 114 MB
"""
class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        MOD = 10**9 + 7

        n = len(edges) + 1
        adj = [[] for _ in range(n + 1)]
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(u: int, f: int) -> int:
            max_dp = 0
            for v in adj[u]:
                if v == f:
                    continue
                max_dp = max(max_dp, dfs(v, u) + 1)
            return max_dp
        
        max_depth = dfs(1, 0)

        return pow(2, max_depth - 1, MOD)

