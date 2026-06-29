"""
Problem Name: Best Time to Buy and Sell Stock with Cooldown
Difficulty: Medium
Tags: Array, Dynamic Programming
"""

"""
Submission 1
Language: python3
Runtime: 4 ms
Memory: 21.3 MB
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # State: Buying or selling
        # If Buy: i + 1
        # If Sell: i + 2
        
        dp = {}     # Key=(i, buying), val=max_profit

        def recur(i: int, buying: bool):
            if i >= len(prices):
                return 0
            
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            if buying:      # If we're in buying state
                buy = recur(i + 1, not buying) - prices[i]        # If we buy at current index
                cooldown = recur(i + 1, buying)
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = recur(i + 2, not buying) + prices[i]
                cooldown = recur(i + 1, buying)
                dp[(i, buying)] = max(sell, cooldown)
            
            return dp[(i, buying)]
        
        return recur(0, True)

