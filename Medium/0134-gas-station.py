"""
Problem Name: Gas Station
Difficulty: Medium
Tags: Array, Greedy
"""

"""
Submission 1
Language: python3
Runtime: 12 ms
Memory: 23.3 MB
"""
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # No solution exists in this case
        if sum(gas) < sum(cost):
            return -1

        # A solution exists 

        ret = 0
        total = 0
        for i in range(len(gas)):
            total += (gas[i] - cost[i])

            if total < 0:
                total = 0
                ret = i + 1
                continue
        # For this starting position, the total never dipped below 0
        # after this position
        return ret

"""
Submission 2
Language: python3
Runtime: 17 ms
Memory: 25.9 MB
"""
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        ret = 0
        total = 0

        for i in range(len(gas)):
            total += (gas[i] - cost[i])

            if total < 0:   # Kadane's
                total = 0
                ret = i + 1
                continue
        
        return ret

"""
Submission 3
Language: python3
Runtime: 12 ms
Memory: 25.9 MB
"""
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Only case of failure
        if sum(gas) < sum(cost):
            return -1
        
        ret = 0
        total = 0

        # A path is guaranteed
        for i in range(len(gas)):
            total += (gas[i] - cost[i])

            # No station before this index can be the correct starting point.
            # Because even though we had a headstart, we still fell below 0 fuel at this point.
            # So we try again at index i + 1
            # So any start index that allows us to reach the end on a net +ve is the valid start point.

            if total < 0:   # Kadane's
                total = 0
                ret = i + 1
                continue
        
        return ret

