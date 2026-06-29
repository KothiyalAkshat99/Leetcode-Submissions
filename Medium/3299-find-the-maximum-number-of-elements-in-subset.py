"""
Problem Name: Find the Maximum Number of Elements in Subset
Difficulty: Medium
Tags: Array, Hash Table, Enumeration
"""

"""
Submission 1
Language: python3
Runtime: 96 ms
Memory: 31.6 MB
"""
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        hashmap = Counter(nums)

        one_count = hashmap.get(1, 0)

        # ret is atleast the number of occurences of 1, rounded down to an odd number
        ret = one_count if one_count % 2 else one_count - 1

        hashmap.pop(1, None)

        for num in hashmap:
            res = 0
            x = num
            while x in hashmap and hashmap[x] > 1:
                res += 2
                x *= x
            ret = max(ret, res + (1 if x in hashmap else -1))
        
        return ret

