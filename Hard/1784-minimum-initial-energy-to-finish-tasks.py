"""
Problem Name: Minimum Initial Energy to Finish Tasks
Difficulty: Hard
Tags: Array, Greedy, Sorting
"""

"""
Submission 1
Language: python3
Runtime: 54 ms
Memory: 55.6 MB
"""
class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)
        start = tasks[0][1]
        bal = tasks[0][1] - tasks[0][0]
        loan = 0

        for i in range(1, len(tasks)):
            cost, thresh = tasks[i]

            if bal < thresh:
                loan += thresh - bal
                bal = thresh
            
            bal -= cost
        
        return start + loan

