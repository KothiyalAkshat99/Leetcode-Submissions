"""
Problem Name: Rotated Digits
Difficulty: Medium
Tags: Math, Dynamic Programming
"""

"""
Submission 1
Language: python3
Runtime: 23 ms
Memory: 19.3 MB
"""
class Solution:
    def rotatedDigits(self, n: int) -> int:
        if n == 1:
            return 0
        
        count = 0
        
        for i in range(1, n + 1):
            num = i
            isValid = True  # If number is valid
            hasChange = False   # If it changes after rotation

            while num > 0:
                digit = num % 10

                if digit in (3, 4, 7):
                    isValid = False
                    break
                
                if digit in (2, 5, 6, 9):
                    hasChange = True
                
                num = num // 10
            
            if isValid and hasChange:
                count += 1
            
        return count

