"""
Problem Name: Perfect Squares
Difficulty: Medium
Tags: Math, Dynamic Programming, Breadth-First Search
"""

"""
Submission 1
Language: python3
Runtime: 3776 ms
Memory: 53.3 MB
"""
class Solution:
    def numSquares(self, n: int) -> int:
        memo = {}

        def recur(rem) -> int:
            if rem == 0:
                return 0
            if rem < 0:
                return float('inf')
            
            if rem in memo:
                return memo[rem]
            
            min_sq = float('inf')

            for i in range(1, math.isqrt(rem) + 1):
                sq = i ** 2
                # 1 count + count of remaining
                count = 1 + recur(rem - sq)
                # Keep track of min count
                min_sq = min(min_sq, count)
            
            memo[rem] = min_sq
            return min_sq
    
        return recur(n)

"""
Submission 2
Language: python3
Runtime: 2037 ms
Memory: 19.2 MB
"""
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            j = 1
            while j ** 2 <= i:
                dp[i] = min(dp[i], dp[i - j ** 2] + 1)
                j += 1
        
        return dp[n]

