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
"""
Submission 2
Language: python3
Runtime: 54 ms
Memory: 17.5 MB
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            x = nums[i]
            y = target - x
            if y in map:
                return [i, map[y]]
            map[x] = i

"""
Submission 3
Language: python3
Runtime: 0 ms
Memory: 18.9 MB
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i in range(len(nums)):
            x = nums[i]
            y = target - x
            if y in hmap:
                return [i, hmap[y]]
            hmap[x] = i

