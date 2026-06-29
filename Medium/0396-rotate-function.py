"""
Problem Name: Rotate Function
Difficulty: Medium
Tags: Array, Math, Dynamic Programming
"""

"""
Submission 1
Language: python3
Runtime: 142 ms
Memory: 31.1 MB
"""
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        
        total_sum = 0
        F = 0
        
        for i in range(n):
            total_sum += nums[i]
            F += i * nums[i]
        
        result = F
        
        for k in range(1, n):
            F = F + total_sum - n * nums[n - k]
            result = max(result, F)
        
        return result

