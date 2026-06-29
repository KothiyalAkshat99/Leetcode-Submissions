"""
Problem Name: Candy
Difficulty: Hard
Tags: Array, Greedy
"""

"""
Submission 1
Language: python3
Runtime: 23 ms
Memory: 21.5 MB
"""
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n   # Each child gets atleast 1 candy

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        
        count = 0       # To track min total candies
        for i in range(n - 1, 0, -1):
            if ratings[i - 1] > ratings[i]:
                candies[i - 1] = max(candies[i] + 1, candies[i - 1])
            count += candies[i - 1]     # Sums up [0, n-2] in candies
        
        return count + candies[n - 1]   # Adding last value 

