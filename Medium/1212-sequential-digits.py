"""
Problem Name: Sequential Digits
Difficulty: Medium
Tags: Enumeration
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 19.2 MB
"""
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ret = []
        for i in range(1, 10):
            num = i
            for j in range(i + 1, 10):
                num = num * 10 + j
                if low <= num <= high:
                    ret.append(num)
        
        ret.sort()
        return ret

