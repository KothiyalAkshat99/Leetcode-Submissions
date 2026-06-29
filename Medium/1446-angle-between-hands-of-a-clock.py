"""
Problem Name: Angle Between Hands of a Clock
Difficulty: Medium
Tags: Math
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 19.4 MB
"""
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour %= 12
        
        # Full Circle = 360
        # Minute hand completes 1 full circle in 60 minutes
        # Each minute represents 6 deg
        minute_angle = minutes * 6.0

        # 12hours, where each hour = 30 deg
        # Hour hand moves 0.5deg every minute
        # This adjusts hour hand movement according to minutes
        hour_angle = hour * 30.0 + minutes * 0.5

        diff = abs(hour_angle - minute_angle)

        return min(diff, 360.0 - diff)

