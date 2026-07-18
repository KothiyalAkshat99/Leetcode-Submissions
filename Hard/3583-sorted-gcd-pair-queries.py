"""
Problem Name: Sorted GCD Pair Queries
Difficulty: Hard
Tags: Array, Hash Table, Math, Binary Search, Combinatorics, Counting, Number Theory, Prefix Sum
"""

"""
Submission 1
Language: python3
Runtime: 499 ms
Memory: 40.1 MB
"""
class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        m = max(nums)

        count = [0] * (m + 1)

        for num in nums:
            count[num] += 1
        
        for i in range(1, m + 1):
            for j in range(i * 2, m + 1, i):
                count[i] += count[j]
        
        for i in range(1, m + 1):
            count[i] = count[i] * (count[i] - 1) // 2
        
        for i in range(m, 0, -1):
            for j in range(i * 2, m + 1, i):
                count[i] -= count[j]
        
        for i in range(1, m + 1):
            count[i] += count[i - 1]

        ret = []
        for q in queries:
            q += 1
            pos = bisect_left(count, q)
            ret.append(pos)
        
        return ret

