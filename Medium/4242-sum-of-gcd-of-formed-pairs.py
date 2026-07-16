"""
Problem Name: Sum of GCD of Formed Pairs
Difficulty: Medium
Tags: Array, Math, Two Pointers, Sorting, Simulation, Number Theory
"""

"""
Submission 1
Language: python3
Runtime: 208 ms
Memory: 36.8 MB
"""
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        mx = []

        prefix_max = -inf

        # Get Max values
        for num in nums:
            prefix_max = max(num, prefix_max)
            mx.append(prefix_max)
        
        prefixGcd = [gcd(x, y) for x, y in zip(nums, mx)]
        prefixGcd.sort()

        ret = 0
        left, right = 0, n - 1
        
        while left < right:
            ret += gcd(prefixGcd[left], prefixGcd[right])
            left += 1
            right -= 1
        
        return ret

