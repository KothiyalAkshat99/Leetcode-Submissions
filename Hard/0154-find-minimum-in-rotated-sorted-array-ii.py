"""
Problem Name: Find Minimum in Rotated Sorted Array II
Difficulty: Hard
Tags: Array, Binary Search
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 19.4 MB
"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        l = 0
        r = n - 1
        ret = nums[l]

        while l <= r:
            m = (l + r) // 2
            
            if nums[m] < nums[r]:
                r = m
            elif nums[m] > nums[r]:
                l = m + 1
            else:   # duplicates
                r -= 1
        
        return nums[l]

