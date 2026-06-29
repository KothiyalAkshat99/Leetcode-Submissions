"""
Problem Name: Running Sum of 1d Array
Difficulty: Easy
Tags: Array, Prefix Sum
"""

"""
Submission 1
Language: python3
Runtime: 51 ms
Memory: 16.6 MB
"""
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i]+=nums[i-1]
        return nums

