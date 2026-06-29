"""
Problem Name: Maximum Sum Circular Subarray
Difficulty: Medium
Tags: Array, Divide and Conquer, Dynamic Programming, Queue, Monotonic Queue
"""

"""
Submission 1
Language: python3
Runtime: 38 ms
Memory: 24.2 MB
"""
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        currmax, currmin = 0, 0
        globmax, globmin = nums[0], nums[0]
        total = 0

        for num in nums:
            currmax = max(currmax + num, num)
            currmin = min(currmin + num, num)

            total += num

            globmax = max(globmax, currmax)
            globmin = min(globmin, currmin)
        
        return max(globmax, total - globmin) if globmax > 0 else globmax

