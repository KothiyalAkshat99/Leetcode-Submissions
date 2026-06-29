"""
Problem Name: Partition Labels
Difficulty: Medium
Tags: Hash Table, Two Pointers, String, Greedy
"""

"""
Submission 1
Language: python3
Runtime: 3 ms
Memory: 17.9 MB
"""
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {} # char -> last found index

        for i, c in enumerate(s):
            lastIndex[c] = i
        
        ret = []
        size, end = 0, 0
        for i, c in enumerate(s):
            size += 1
            if lastIndex[c] > end:
                end = lastIndex[c]
            
            if i == end:
                ret.append(size) # a partition has been completed
                size = 0 # for new partition
        
        return ret

"""
Submission 2
Language: python3
Runtime: 3 ms
Memory: 19.2 MB
"""
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurence = defaultdict(int)
        ret = []

        for i, char in enumerate(s):
            last_occurence[char] = i
        
        partition_size = 0
        partition_end = 0
        for i, char in enumerate(s):
            partition_size += 1
            # If any char in current partition has last_idx > curr_end
            if last_occurence[char] > partition_end:
                partition_end = last_occurence[char]
            
            if i == partition_end:  # A partition has been completed
                ret.append(partition_size)
                partition_size = 0
        
        return ret

