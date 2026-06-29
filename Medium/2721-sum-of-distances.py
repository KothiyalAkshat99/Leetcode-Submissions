"""
Problem Name: Sum of Distances
Difficulty: Medium
Tags: Array, Hash Table, Prefix Sum
"""

"""
Submission 1
Language: python3
Runtime: 122 ms
Memory: 54.9 MB
"""
class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        hashmap = defaultdict(list)    # value:[indices]
        for i, num in enumerate(nums):
            hashmap[num].append(i)
        
        ret = [0] * len(nums)
        
        for val in hashmap.values():
            total = sum(val)
            l_sum = 0
            m = len(val)

            for i in range(m):
                r_sum = total - l_sum - val[i]

                left = val[i] * i - l_sum
                right = r_sum - val[i] * (m - i - 1)

                ret[val[i]] = left + right

                l_sum += val[i]
            
        return ret

