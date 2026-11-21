"""
Problem Name: Replace Elements with Greatest Element on Right Side
Difficulty: Easy
Tags: Array
"""
"""
Submission 1
Submission ID: 2198145173
Language: python3
Runtime: 18 ms
Memory: 20.5 MB
Submitted: 2026-11-17T16:43:48.000Z
"""
class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        greatest_to_right = -1

        for i in range(len(arr) - 1, -1, -1):
            arr[i], greatest_to_right = greatest_to_right, max(greatest_to_right, arr[i])
        
        return arr
"""
Submission 2
Language: python3
Runtime: 18 ms
Memory: 20.4 MB
"""
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            return [-1]
        
        n = len(arr)
        curr_max = arr[n - 1]
        
        for i in range(n - 2, -1, -1):
            temp = arr[i]
            arr[i] = curr_max
            if temp > curr_max:
                curr_max = temp
        
        arr[-1] = -1
        return arr

