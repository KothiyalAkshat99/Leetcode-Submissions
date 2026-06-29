"""
Problem Name: Maximum Element After Decreasing and Rearranging
Difficulty: Medium
Tags: Array, Greedy, Sorting
"""

"""
Submission 1
Language: python3
Runtime: 22 ms
Memory: 28.3 MB
"""
class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        ret = 1     # 1 has to be in the final arr

        for i in range(1, len(arr)):
            # In the sorted array,
            # every time (num - curr_max) >= 1, we increase curr_max by 1
            if arr[i] >= ret + 1:
                ret += 1
        
        return ret

