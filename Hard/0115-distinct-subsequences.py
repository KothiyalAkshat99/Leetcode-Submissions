"""
Problem Name: Distinct Subsequences
Difficulty: Hard
Tags: String, Dynamic Programming
"""

"""
Submission 1
Language: python3
Runtime: 19 ms
Memory: 44 MB
"""
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(t) > len(s):
            return 0
        n, m = len(s), len(t)
        dp = [[-1] * (m + 1) for _ in range(n + 1)]     # (i, j): count

        def recur(i: int, j: int) -> int:
            # if s2 exhausted - matched SUCCESSFULLY
            if j >= m:
                return 1
            
            # if s1 exhausted but s2 is not
            # Cannot be matched
            if i >= n:
                return 0

            # len(remaining substr of s) < len(remaining substr of t)
            # Cannot be matched
            if n - i < m - j:
                return 0
            
            # Memoization
            if dp[i][j] != -1:
                return dp[i][j]
            
            ret = 0

            # If characters at i and j match
            if s[i] == t[j]:
                # Choose matching character from s1
                # or 
                # ignore character in s1 and move to next
                ret = recur(i + 1, j + 1) \
                        + \
                        recur(i + 1, j)
            else:
                # Skip current char in s1 and move to next
                ret = recur(i + 1, j)
            
            dp[i][j] = ret
            return ret
        
        return recur(0, 0)

"""
Submission 2
Language: python3
Runtime: 440 ms
Memory: 75.4 MB
"""
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(t) > len(s):
            return 0
        n, m = len(s), len(t)
        dp = [[0] * (m + 1) for _ in range(n + 1)]     # (i, j): count

        for i in range(n + 1):
            dp[i][m] = 1

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                dp[i][j] = dp[i + 1][j]

                if s[i] == t[j]:
                    dp[i][j] += dp[i + 1][j + 1]
        
        return dp[0][0]

"""
Submission 3
Language: python3
Runtime: 445 ms
Memory: 75.6 MB
"""
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]

        for i in range(0, len(s) + 1):
            dp[i][0] = 1                # base case: for empty target t, there is only one way: ignore the char in s
        
        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):

                s_char = s[i - 1]
                t_char = t[j - 1]

                if s_char != t_char:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] =  dp[i - 1][j] + dp[i - 1][j - 1] # skip current s char, or use current s char

        return dp[len(s)][len(t)]

