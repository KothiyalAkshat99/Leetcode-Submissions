"""
Problem Name: Minimum Cost of Buying Candies With Discount
Difficulty: Easy
Tags: Array, Greedy, Sorting
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 19.2 MB
"""
class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        if len(cost) == 1:
            return cost[0]
        if len(cost) == 2:
            return cost[0] + cost[1]
        
        cost.sort(reverse=True)
        count = 2
        ret = 0
        for i, c in enumerate(cost):
            if count:
                ret += c
                count -= 1
            else:
                count = 2
                continue
        
        return ret

