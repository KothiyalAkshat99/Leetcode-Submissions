"""
Problem Name: Count Subarrays With Majority Element I
Difficulty: Medium
Tags: Array, Hash Table, Divide and Conquer, Segment Tree, Merge Sort, Counting, Prefix Sum
"""

"""
Submission 1
Language: python3
Runtime: 1873 ms
Memory: 19.4 MB
"""
class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ret = 0

        for i in range(n):
            target_count = 0

            for j in range(i, n):
                if nums[j] == target:
                    target_count += 1
                #else:
                    #target_count -= 1
                
                subset_len = j - i + 1

                if target_count > subset_len // 2:
                    ret += 1
        
        return ret

"""
Submission 2
Language: python3
Runtime: 1336 ms
Memory: 19.5 MB
"""
class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ret = 0

        # Boyer-Moore Majority Voting Algo
        for i in range(n):
            target_count = 0

            for j in range(i, n):
                if nums[j] == target:
                    target_count += 1
                else:
                    target_count -= 1
                
                if target_count > 0:
                    ret += 1
        
        return ret

