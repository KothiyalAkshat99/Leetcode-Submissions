"""
Problem Name: Jump Game II
Difficulty: Medium
Tags: Array, Dynamic Programming, Greedy
"""

"""
Submission 1
Language: python3
Runtime: 7 ms
Memory: 18.8 MB
"""
class Solution:
    def jump(self, nums: List[int]) -> int:
        # GREEDY BFS

        ret = 0 # Counting number of jumps
        l = r = 0 # Window of jump, being considered for BFS

        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                # Who can jump the farthest
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            ret += 1
        
        return ret

"""
Submission 2
Language: python3
Runtime: 7 ms
Memory: 20.1 MB
"""
class Solution:
    def jump(self, nums: List[int]) -> int:
        near = far = jumps = 0

        while far < len(nums) - 1:
            farthest = 0
            for i in range(near, far + 1):
                farthest = max(farthest, i + nums[i])
            
            near = far + 1
            far = farthest
            jumps += 1
        
        return jumps

"""
Submission 3
Language: python3
Runtime: 5 ms
Memory: 20 MB
"""
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        # At each index, need to see what's the max reach we can get?
        # Only increase jump count if new reach > current reach
        curr_jump_end = 0
        reach = 0
        jumps = 0
        for i in range(len(nums) - 1):
            # Keeping track of absolute farthest we can reach
            reach = max(reach, i + nums[i])

            # If we've reached end of current jump's radius
            if i == curr_jump_end:
                jumps += 1
                curr_jump_end = reach   # New jump radius
            
            if curr_jump_end >= len(nums) - 1:
                break
        
        return jumps

