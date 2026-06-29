"""
Problem Name: Find the Highest Altitude
Difficulty: Easy
Tags: Array, Prefix Sum
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 19.1 MB
"""
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = 0
        max_alt = 0

        for val in gain:
            altitude += val
            max_alt = max(altitude, max_alt)
        
        return max_alt

