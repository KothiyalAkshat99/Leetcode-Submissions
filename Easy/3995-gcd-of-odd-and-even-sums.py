"""
Problem Name: GCD of Odd and Even Sums
Difficulty: Easy
Tags: Math, Number Theory
"""

"""
Submission 1
Language: python3
Runtime: 35 ms
Memory: 19.8 MB
"""
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumEven, sumOdd = 0, 0
        odd, even = 1, 2
        
        while n:
            sumOdd += odd
            sumEven += even
            
            odd += 2
            even += 2

            n -= 1
        
        def gcd(x: int, y: int) -> int:
            return x if y == 0 else gcd(y, x % y)
        
        return gcd(sumOdd, sumEven)

