"""
Problem Name: Jump Game VII
Difficulty: Medium
Tags: String, Dynamic Programming, Sliding Window, Prefix Sum
"""

"""
Submission 1
Language: python3
Runtime: 133 ms
Memory: 20.5 MB
"""
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] != '0':
            return False
        
        n = len(s)

        dp = [False] * n
        dp[0] = True

        reachable = 0

        for i in range(1, n):
            if i >= minJump and dp[i - minJump]:
                reachable += 1
            
            if i > maxJump and dp[i - maxJump - 1]:
                reachable -= 1
            
            if reachable > 0 and s[i] == '0':
                dp[i] = True
        
        return dp[-1]

