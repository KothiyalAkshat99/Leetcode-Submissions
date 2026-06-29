"""
Problem Name: Combination Sum IV
Difficulty: Medium
Tags: Array, Dynamic Programming
"""

"""
Submission 1
Language: python3
Runtime: 50 ms
Memory: 19.3 MB
"""
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        
        for i in range(1, target + 1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i - num]
                    
        return dp[target]

"""
Submission 2
Language: python3
Runtime: 41 ms
Memory: 19.4 MB
"""
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        #dp = [0] * (target + 1) # Num ways in which we can reach target sums
        nums.sort()
        memo = {}

        def recur(n):
            if n in memo:
                return memo[n]
            if n == 0:
                return 1
            if n < nums[0]:
                return 0
            
            count = 0
            for num in nums:
                if n - num < 0:
                    break
                count += recur(n - num)
            
            memo[n] = count
            return count
        
        return recur(target)

