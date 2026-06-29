"""
Problem Name: Earliest Finish Time for Land and Water Rides I
Difficulty: Easy
Tags: Array, Two Pointers, Binary Search, Greedy, Sorting
"""

"""
Submission 1
Language: python3
Runtime: 287 ms
Memory: 19.3 MB
"""
class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        # Brute Force
        n = len(landStartTime)
        m = len(waterStartTime)
        ret = inf

        for i in range(n):
            for j in range(m):
                land = landStartTime[i] + landDuration[i]
                land_water = max(land, waterStartTime[j]) + waterDuration[j]
                ret = min(ret, land_water)

                water = waterStartTime[j] + waterDuration[j]
                water_land = max(water, landStartTime[i]) + landDuration[i]
                ret = min(ret, water_land)
        
        return ret

"""
Submission 2
Language: python3
Runtime: 15 ms
Memory: 19.4 MB
"""
class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        # Find Earliest for Land, then use it to find min overall
        # Reverse -> Earliest water, then find min overall

        def solve(st1: list, dur1: list, st2: list, dur2: list):
            fin1 = inf
            for i in range(len(st1)):
                fin1 = min(fin1, st1[i] + dur1[i])
            
            fin2 = inf
            for i in range(len(st2)):
                fin2 = min(fin2, max(st2[i], fin1) + dur2[i])
            
            return fin2
        
        land_water = solve(landStartTime, landDuration, waterStartTime, waterDuration)
        
        water_land = solve(waterStartTime, waterDuration, landStartTime, landDuration)

        return min(land_water, water_land)

