"""
Problem Name: Maximum Ice Cream Bars
Difficulty: Medium
Tags: Array, Greedy, Sorting, Counting Sort
"""

"""
Submission 1
Language: python3
Runtime: 84 ms
Memory: 32 MB
"""
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        if coins < costs[0]:
            return 0
        
        count = 0
        for cost in costs:
            if cost <= coins:
                coins -= cost
                count += 1
            else:
                break
        
        return count

