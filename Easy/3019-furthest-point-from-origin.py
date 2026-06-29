"""
Problem Name: Furthest Point From Origin
Difficulty: Easy
Tags: String, Counting
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 19.3 MB
"""
class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        ret = 0
        temp = 0
        for move in moves:
            if move == 'L':
                ret -= 1
            elif move == 'R':
                ret += 1
            elif move == '_':
                temp += 1
        
        return abs(ret) + temp

