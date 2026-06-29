"""
Problem Name: Longest Harmonious Subsequence
Difficulty: Easy
Tags: Array, Hash Table, Sliding Window, Sorting, Counting
"""

"""
Submission 1
Language: python3
Runtime: 236 ms
Memory: 18.3 MB
"""
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        hmap = dict()
        
        for i in nums:
            if i in hmap:
                hmap[i] += 1
                continue
            
            hmap[i] = 1
        
        #print(hmap)

        maxct = 0

        for i in hmap:
            if i+1 in hmap:
                maxct = max(maxct, hmap[i] + hmap[i+1])

        return maxct

