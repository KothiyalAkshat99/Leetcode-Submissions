"""
Problem Name: Find the Length of the Longest Common Prefix
Difficulty: Medium
Tags: Array, Hash Table, String, Trie
"""

"""
Submission 1
Language: python3
Runtime: 350 ms
Memory: 36.5 MB
"""
class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, num) -> None:
        node = self.root
        for digit in str(num):
            if digit not in node.children:
                node.children[digit] = TrieNode()
            node = node.children[digit]
    
    def findLongestPrefix(self, num) -> int:
        l = 0
        node = self.root

        for digit in str(num):
            if digit in node.children:
                l += 1
                node = node.children[digit]
                continue
            break
        
        return l

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie = Trie()

        for num in arr1:
            trie.insert(num)
        
        ret = 0     # Longest Prefix -> return value

        for num in arr2:
            l = trie.findLongestPrefix(num)
            ret = max(ret, l)
        
        return ret

"""
Submission 2
Language: python3
Runtime: 183 ms
Memory: 30 MB
"""
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes = set()

        # Add all prefixes of all numbers from arr1 into a set
        for num in arr1:
            x = num
            while x > 0:
                prefixes.add(x)
                x = x // 10
        
        ret = 0

        for num in arr2:
            y = num
            while y > 0:
                if y in prefixes:
                    l = len(str(y))
                    ret = max(ret, l)
                    break
                y = y // 10
        
        return ret

