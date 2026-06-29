"""
Problem Name: Longest Common Suffix Queries
Difficulty: Hard
Tags: Array, String, Trie
"""

"""
Submission 1
Language: python3
Runtime: 2251 ms
Memory: 180.5 MB
"""
class TrieNode:
    def __init__(self):
        self.children = {}
        # Index of shortest inserted string passing thru this node
        self.index = float('inf')
        self.min_len = float('inf')

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str, index: int):
        curr = self.root
        if len(word) < curr.min_len:
            curr.min_len = len(word)
            curr.index = index

        # Word has been pre-reversed
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]

            if len(word) < curr.min_len:
                curr.min_len = len(word)
                curr.index = index

    def query(self, word: str) -> int:
        curr = self.root
        
        for ch in word:
            if ch in curr.children:
                curr = curr.children[ch]
            else:
                break
        
        return curr.index


class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        trie = Trie()

        # Build trie using reversed words
        for i, word in enumerate(wordsContainer):
            rev_word = word[::-1]
            trie.insert(rev_word, i)
        
        ret = []
        for query in wordsQuery:
            rev_q = query[::-1] # Reverse query
            ret.append(trie.query(rev_q))

        return ret

