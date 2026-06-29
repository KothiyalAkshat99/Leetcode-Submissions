"""
Problem Name: Words Within Two Edits of Dictionary
Difficulty: Medium
Tags: Array, String, Trie
"""

"""
Submission 1
Language: python3
Runtime: 27 ms
Memory: 22.2 MB
"""
class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
    
    def insert(self, word) -> None:
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        
        curr.isEnd = True

    def checkQuery(self, word, i, node, count) -> bool:
        # DFS
        if count > 2 or not node:
            return False
        
        if i == len(word):
            return node.isEnd
        
        # No changes made
        if word[i] in node.children and self.checkQuery(word, i + 1, node.children[word[i]], count):
            return True
        
        # Changes made
        if count < 2:
            for next_char, child_node in node.children.items():
                # We only want to explore paths that require a change 
                if next_char != word[i]:
                    # Recurse, incrementing the edit count
                    if self.checkQuery(word, i + 1, child_node, count + 1):
                        return True
                        
        return False        

class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        ret = []
        dictionary = set(dictionary)
        trie = Trie()

        # Build Trie from dictionary
        for word in dictionary:
            trie.insert(word)
        
        # Iterate over queries
        for query in queries:
            if query in dictionary:
                ret.append(query)
                continue

            # Check for query in Trie
            if trie.checkQuery(query, 0, trie.root, 0):
                ret.append(query)
            
        return ret

