"""
Problem Name: Find the Prefix Common Array of Two Arrays
Difficulty: Medium
Tags: Array, Hash Table, Bit Manipulation
"""

"""
Submission 1
Language: python3
Runtime: 3 ms
Memory: 17.9 MB
"""
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        hmap = {}
        C = []
        c = 0
        for i in range(0, len(A)):
            
            if A[i] not in hmap:
                hmap[A[i]] = 1
            else:
                c = c+1
                del hmap[A[i]]
            
            if B[i] not in hmap:
                hmap[B[i]] = 1
            else:
                c = c+1
                del hmap[B[i]]
            
            C.append(c)
        
        return C


"""
Submission 2
Language: python3
Runtime: 6 ms
Memory: 19.3 MB
"""
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        if len(A) == 1:
            return [1]
        
        hashmap = defaultdict(int)
        count = 0
        ret = []

        for i in range(len(A)):
            hashmap[A[i]] += 1
            if hashmap[A[i]] == 2:
                count += 1
            hashmap[B[i]] += 1
            if hashmap[B[i]] == 2:
                count += 1
            
            ret.append(count)
        
        return ret


