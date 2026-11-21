"""
Problem Name: Two Sum
Difficulty: Easy
Tags: Array, Hash Table
"""
"""
Submission 1
Submission ID: lc2gh-fixture-001
Language: python3
Runtime: 48 ms
Memory: 15.1 MB
Submitted: 2026-10-19T00:00:00.000Z
"""
class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for index, value in enumerate(nums):
            complement = target - value
            if complement in seen:
                return [seen[complement], index]
            seen[value] = index
        return []