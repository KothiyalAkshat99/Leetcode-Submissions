"""
Problem Name: Stone Game III
Difficulty: Hard
Tags: Array, Math, Dynamic Programming, Game Theory
"""

"""
Submission 1
Language: python3
Runtime: 1692 ms
Memory: 169.3 MB
"""
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        dp = {}

        # Returns (alice-bob) OR (bob-alice) -> based on turn
        def dfs(i) -> int:
            if i == len(stoneValue):
                return 0
            if i in dp:
                return dp[i]
            
            ret = float("-inf")
            for j in range(i, min(i + 3, len(stoneValue))):
                ret = max(ret, sum(stoneValue[i:j+1]) - dfs(j + 1))
            
            dp[i] = ret
            return ret
        
        return "Alice" if dfs(0) > 0 else ("Bob" if dfs(0) < 0 else "Tie")

