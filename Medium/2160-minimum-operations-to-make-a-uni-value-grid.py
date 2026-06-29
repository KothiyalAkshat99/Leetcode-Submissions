"""
Problem Name: Minimum Operations to Make a Uni-Value Grid
Difficulty: Medium
Tags: Array, Math, Sorting, Matrix
"""

"""
Submission 1
Language: python3
Runtime: 163 ms
Memory: 40.8 MB
"""
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = []
        ret = 0

        for row in grid:
            for n in row:
                nums.append(n)

        # Need to find median
        nums.sort()
        n = len(nums)

        median = nums[n // 2]

        for num in nums:
            # If remainder when dividing by x is different, return -1
            if num % x != median % x:
                return -1
            
            # Number of operations required to make (curr_num == median)
            ret += abs(median - num) // x
        
        return ret

