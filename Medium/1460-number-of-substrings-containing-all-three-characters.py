"""
Problem Name: Number of Substrings Containing All Three Characters
Difficulty: Medium
Tags: Hash Table, String, Sliding Window
"""

"""
Submission 1
Language: python3
Runtime: 123 ms
Memory: 19.4 MB
"""
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # If a substring from l to r is valid,
        # then EVERY SUBSTRING that starts at l and ends ANYWHERE after r is VALID TOO obv.
        # So we're not checking each and every substring but deducing mathematically.

        # For 'abcabc'
        # If l = 0, r = 2, substring = 'abc'
        # then every substring starting at l and ending ANYWHERE after r is VALID too.
        # So we increase count by (n - r)
        # And then shrink window (increase l by 1, so as to now check from next l)
        count = 0
        hashmap = defaultdict(int)
        l, r = 0, 0

        while r < len(s):
            hashmap[s[r]] += 1
            
            while hashmap['a'] > 0 and hashmap['b'] > 0 and hashmap['c'] > 0:
                # All substrings from current window to end are valid
                # Add count of valid substrings
                count += len(s) - r

                # Shrink the window from left
                hashmap[s[l]] -= 1
                l += 1
            
            r += 1
        
        return count

