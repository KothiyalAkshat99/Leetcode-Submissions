"""
Problem Name: Longest Turbulent Subarray
Difficulty: Medium
Tags: Array, Dynamic Programming, Sliding Window
"""

"""
Submission 1
Language: python3
Runtime: 60 ms
Memory: 23.2 MB
"""
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1
        
        n = len(arr)
        ret = 1
        left = 0

        def compare(x: int, y: int) -> int:
            if x < y:
                return -1
            if x > y:
                return 1
            return 0
        
        for i in range(1, n):
            c = compare(arr[i - 1], arr[i])

            if c == 0:
                left = i
            else:
                if i == n - 1 or \
                    c * compare(arr[i], arr[i + 1]) != -1:
                    ret = max(ret, i - left + 1)
                    left = i
        
        return ret

