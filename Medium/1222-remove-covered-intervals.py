"""
Problem Name: Remove Covered Intervals
Difficulty: Medium
Tags: Array, Sorting
"""

"""
Submission 1
Language: python3
Runtime: 1 ms
Memory: 18.1 MB
"""
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i: (i[0], -i[1])) # ASC interval start, DESC interval end

        res = [intervals[0]]

        for l, r in intervals[1:]:
            prevL, prevR = res[-1]

            if prevL <= l and prevR >= r:
                continue
            
            res.append([l, r])

        return len(res)

"""
Submission 2
Language: python3
Runtime: 5 ms
Memory: 19.7 MB
"""
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # Interval Start in ASC, Interval End in Desc
        intervals.sort(key = lambda i: (i[0], -i[1]))

        stack = [intervals[0]]

        for i in range(1, len(intervals)):
            l, r = intervals[i]
            prev_l, prev_r = stack[-1]

            # Current intervals [l, r] is covered already, so continue
            if prev_l <= l and prev_r >= r:
                continue
            
            stack.append([l, r])
        
        return len(stack)

