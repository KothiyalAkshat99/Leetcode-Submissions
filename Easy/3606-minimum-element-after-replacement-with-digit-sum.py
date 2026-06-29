"""
Problem Name: Minimum Element After Replacement With Digit Sum
Difficulty: Easy
Tags: Array, Math
"""

"""
Submission 1
Language: python3
Runtime: 8 ms
Memory: 19.4 MB
"""
class Solution:
    def minElement(self, nums: List[int]) -> int:
        ret = float('inf')

        for num in nums:
            num_sum = 0
            x = num
            while x:
                num_sum += x % 10
                x = x // 10
            ret = min(ret, num_sum)
        
        return ret

