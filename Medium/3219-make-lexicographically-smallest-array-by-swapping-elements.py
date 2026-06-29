"""
Problem Name: Make Lexicographically Smallest Array by Swapping Elements
Difficulty: Medium
Tags: Array, Union-Find, Sorting
"""

"""
Submission 1
Language: python3
Runtime: 241 ms
Memory: 95.4 MB
"""
class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        groups = []
        num_to_group = {}     # nums[i] -> groups index

        for num in sorted(nums):
            if not groups or abs(num - groups[-1][-1]) > limit:
                groups.append(deque())
            
            groups[-1].append(num)
            num_to_group[num] = len(groups) - 1
        
        ret = []

        for num in nums:
            j = num_to_group[num]
            ret.append(groups[j].popleft())
        
        return ret

