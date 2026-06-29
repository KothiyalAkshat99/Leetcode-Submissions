"""
Problem Name: Last Stone Weight II
Difficulty: Medium
Tags: Array, Dynamic Programming
"""

"""
Submission 1
Language: python3
Runtime: 31 ms
Memory: 27 MB
"""
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # KNAPSACK
        n = len(stones)
        sum_stones = sum(stones)
        target = ceil(sum_stones / 2)

        # Suppose sum of stones = 23
        # Thru dfs, we find a total of 12.
        # Means there's another half with total of 11
        # Therefore, difference would be 23-12 == 12-11 == 0

        dp = {}

        def dfs(i: int, curr_total: int):
            if curr_total >= target or i == len(stones):
                return abs(curr_total - (sum_stones - curr_total))
            
            if (i, curr_total) in dp:
                return dp[(i, curr_total)]
            
            dp[(i, curr_total)] = min(
                dfs(i + 1, curr_total), # Not taking current stone
                dfs(i + 1, curr_total + stones[i])  # Take current stone
            )
            
            return dp[(i, curr_total)]
            
        return dfs(0, 0)

