"""
Problem Name: Divide Array in Sets of K Consecutive Numbers
Difficulty: Medium
Tags: Array, Hash Table, Greedy, Sorting
"""

"""
Submission 1
Language: python3
Runtime: 128 ms
Memory: 37.4 MB
"""
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False

        hashset = Counter(nums)

        for num in nums:
            start_set = num

            # Find potential start of set 
            while hashset[start_set - 1]:
                start_set -= 1
            
            while start_set <= num:
                while hashset[start_set]:
                    for next_card in range(start_set, start_set + k):
                        if not hashset[next_card]:
                            return False
                        hashset[next_card] -= 1
                start_set += 1
        
        return True

