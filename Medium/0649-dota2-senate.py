"""
Problem Name: Dota2 Senate
Difficulty: Medium
Tags: String, Greedy, Queue
"""

"""
Submission 1
Language: python3
Runtime: 11 ms
Memory: 19.6 MB
"""
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r, d = deque(), deque()
        n = len(senate)

        for i, sen in enumerate(senate):
            if sen == 'R':
                r.append(i)
            elif sen == 'D':
                d.append(i)
        
        while r and d:
            r_idx = r.popleft()
            d_idx = d.popleft()

            if r_idx < d_idx:       # r won this round
                r.append(r_idx + n)
            else:                   # d won this round
                d.append(d_idx + n)
        
        return 'Radiant' if r else 'Dire'

