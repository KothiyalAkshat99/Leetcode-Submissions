"""
Problem Name: Check if Array Is Sorted and Rotated
Difficulty: Easy
Tags: Array
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 19.2 MB
"""
class Solution:
    def check(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        flag = 0
        n = len(nums)

        for i in range(1, n):
            if nums[i] < nums[i - 1]:   # First index where i < i-1
                for j in range(i, n - 1):   # Non-decr from here
                    if nums[j] > nums[j + 1]:
                        return False
                
                return nums[n - 1] <= nums[0]
        
        return True

