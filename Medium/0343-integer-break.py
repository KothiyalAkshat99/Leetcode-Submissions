"""
Problem Name: Integer Break
Difficulty: Medium
Tags: Math, Dynamic Programming
"""

"""
Submission 1
Language: python3
Runtime: 3 ms
Memory: 19.4 MB
"""
class Solution:
    def integerBreak(self, n: int) -> int:
        memo = {}

        def recur(k):
            if k in memo:
                return memo[k]
            if k == 1:
                return 1
            ret = -float('inf')
            for i in range(1, k):
                ret = max(ret, i * recur(k - i), i * (k - i))
            
            memo[k] = ret
            return ret
        
        return recur(n)

