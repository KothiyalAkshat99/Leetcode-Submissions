"""
Problem Name: Maximum Subarray
Difficulty: Medium
Tags: Array, Divide and Conquer, Dynamic Programming
"""

"""
Submission 1
Language: python3
Runtime: 504 ms
Memory: 30.9 MB
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxsum = nums[0]
        cursum = 0

        for i in nums:
            if cursum < 0:
                cursum = 0
            
            cursum += i
            maxsum = max(maxsum, cursum)
        
        return maxsum

"""
Submission 2
Language: python3
Runtime: 51 ms
Memory: 32 MB
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        maxsum = nums[0]
        currsum = maxsum

        for i in range(1, len(nums)):
            if currsum < 0:
                currsum = 0
            currsum += nums[i]
            maxsum = max(maxsum, currsum)

        return maxsum

"""
Submission 3
Language: python3
Runtime: 30 ms
Memory: 31.2 MB
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        currsum = 0
        maxsum = float('-inf')

        for num in nums:
            currsum = max(num, currsum + num)
            maxsum = max(maxsum, currsum)
        
        return maxsum

