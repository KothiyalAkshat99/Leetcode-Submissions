"""
Problem Name: Coin Change II
Difficulty: Medium
Tags: Array, Dynamic Programming
"""

"""
Submission 1
Language: python3
Runtime: 1564 ms
Memory: 374.7 MB
"""
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        ret = 0
        memo = {}

        def recur(i: int, a: int):
            if a == amount:
                return 1
            if a > amount:
                return 0
            if i == len(coins):
                return 0
            if (i, a) in memo:
                return memo[(i, a)]
            
            # Take current coin + Skip current coin
            memo[(i, a)] = recur(i, a + coins[i]) + \
                            recur(i + 1, a)
            
            return memo[(i, a)]
        
        return recur(0, 0)

"""
Submission 2
Language: python3
Runtime: 526 ms
Memory: 65.4 MB
"""
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 1

        for i in range(1, n + 1):
            for j in range(1, amount + 1):
                if coins[i - 1] <= j:
                    dp[i][j] = dp[i][j - coins[i - 1]] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        
        return dp[n][amount]

