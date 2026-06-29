"""
Problem Name: Smallest String With Swaps
Difficulty: Medium
Tags: Array, Hash Table, String, Depth-First Search, Breadth-First Search, Union-Find, Sorting
"""

"""
Submission 1
Language: python3
Runtime: 127 ms
Memory: 62.6 MB
"""
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        # Each index represents a vertex
        # Each pair (i, j) is an undirected edge between vertices i and j
        # Use DFS to traverse each component and collect:
        #   1. Characters corresponding to those indices
        #   2. Indices themselves
        # SORT both characters and their indices (for each connected component)
        # Place sorted characters back into result array at sorted indices
         
        adj = defaultdict(list)
        visited = set()

        for u, v in pairs:
            adj[u].append(v)
            adj[v].append(u)
        
        # Explores connected components
        def dfs(vertex: int, characters: list, indices: list) -> None:
            characters.append(s[vertex])
            indices.append(vertex)

            for nb in adj[vertex]:
                if nb not in visited:
                    visited.add(nb)
                    dfs(nb, characters, indices)
        
        ret = [''] * len(s)
        
        # Explores all components
        for idx, char in enumerate(s):
            if idx not in visited:
                visited.add(idx)
                characters, indices = [], []
                dfs(idx, characters, indices)

                # Sort and Re-assign smallest possible characters
                characters.sort()
                indices.sort()

                for i in range(len(indices)):
                    ret[indices[i]] = characters[i]
        
        return ''.join(ret)

