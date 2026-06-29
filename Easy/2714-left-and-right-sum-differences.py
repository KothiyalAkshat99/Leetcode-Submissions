"""
Problem Name: Left and Right Sum Differences
Difficulty: Easy
Tags: Array, Prefix Sum
"""

"""
Submission 1
Language: python3
Runtime: 3 ms
Memory: 19.2 MB
"""
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ret = [0] * n

        left_sum = 0
        for i in range(n):
            ret[i] = left_sum
            left_sum += nums[i]
        
        right_sum = 0
        for i in range(n - 1, -1, -1):
            ret[i] = abs(ret[i] - right_sum)
            right_sum += nums[i]
        
        return ret

