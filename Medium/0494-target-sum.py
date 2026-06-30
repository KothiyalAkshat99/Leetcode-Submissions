"""
Problem Name: Target Sum
Difficulty: Medium
Tags: Array, Dynamic Programming, Backtracking
"""

"""
Submission 1
Language: python3
Runtime: 187 ms
Memory: 74.4 MB
"""
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # State = (index, currentSum)
        memo = {}

        def recur(idx: int, curr_sum: int) -> int:
            # Base Cases -> If last index reached -> if currentSum == target or not
            if idx == len(nums):
                return 1 if curr_sum == target else 0
            
            if (idx, curr_sum) in memo:
                return memo[(idx, curr_sum)]

            # Decisions
            positive = recur(idx + 1, curr_sum + nums[idx])
            negative = recur(idx + 1, curr_sum - nums[idx])

            # storing (pos + neg) as we're trying to count total number of ways
            memo[(idx, curr_sum)] = positive + negative

            return memo[(idx, curr_sum)]
        
        return recur(0, 0)

