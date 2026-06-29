"""
Problem Name: Largest Number After Digit Swaps by Parity
Difficulty: Easy
Tags: Sorting, Heap (Priority Queue)
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 19.4 MB
"""
class Solution:
    def largestInteger(self, num: int) -> int:
        odd_maxheap = []
        even_maxheap = []
        num = str(num)
        n = len(num)

        for char in num:
            if int(char) % 2 == 0:
                even_maxheap.append(int(char))
            else:
                odd_maxheap.append(int(char))
        
        heapq.heapify_max(even_maxheap)
        heapq.heapify_max(odd_maxheap)

        ret = []
        for idx in range(n):
            if int(num[idx]) % 2 == 0:
                digit = heapq.heappop_max(even_maxheap)
            else:
                digit = heapq.heappop_max(odd_maxheap)
            ret.append(str(digit))
        
        return int(''.join(ret))

