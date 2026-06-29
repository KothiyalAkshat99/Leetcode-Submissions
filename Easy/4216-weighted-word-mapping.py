"""
Problem Name: Weighted Word Mapping
Difficulty: Easy
Tags: Array, String, Simulation
"""

"""
Submission 1
Language: python3
Runtime: 7 ms
Memory: 19.3 MB
"""
class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ret = []
        for word in words:
            s = 0
            for c in word:
                s += weights[ord(c) - ord('a')]
            ret.append(chr(ord('z') - s % 26))
        
        return "".join(ret)

