"""
Problem Name: Stone Game II
Difficulty: Medium
Tags: Array, Math, Dynamic Programming, Prefix Sum, Game Theory
"""

"""
Submission 1
Language: python3
Runtime: 464 ms
Memory: 34.1 MB
"""
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        memo = {}
        def recur(idx: int, M: int, alice: bool) -> int:
            if idx == len(piles):
                return 0
            
            if (idx, M, alice) in memo:
                return memo[(idx, M, alice)]

            ret = 0 if alice else float('inf')

            total = 0
            for X in range(1, 2 * M + 1):
                if idx + X > len(piles):
                    break

                total += piles[idx + X - 1]

                if alice:
                    ret = max(
                        ret, \
                        total + recur(idx + X, max(M, X), not alice)
                        )
                else:
                    ret = min(
                        ret, \
                        recur(idx + X, max(M, X), not alice)
                        )
            
            memo[(idx, M, alice)] = ret
            return ret
        
        return recur(0, 1, True)    # Turn = True(Alice), False(Bob)

