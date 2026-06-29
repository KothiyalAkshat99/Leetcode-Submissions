"""
Problem Name: Process String with Special Operations II
Difficulty: Hard
Tags: String, Simulation
"""

"""
Submission 1
Language: python3
Runtime: 367 ms
Memory: 20.4 MB
"""
class Solution:
    def processStr(self, s: str, k: int) -> str:
        # Length of result can reach 10**15
        # Therefore impossible to explicitly construct

        # We work backwards to find which pos in an earlier state of \
        # result corresponds to k
        # Since final length is unknown, we only simulate length

        length = 0
        # Simulating only length of result, not the actual string
        for char in s:
            if 97 <= ord(char) <= 122:
                length += 1
            elif char == '*':
                if length:
                    length -= 1
            elif char == '#':
                length *= 2
            elif char == '%':
                pass
        
        # If explicitly OOB
        if k + 1 > length:
            return '.'
        
        # We traverse 's' from R to L
        # and reverse each operation
        # '*' now makes length + 1 since it deleted a char earlier
        # '#'
        # '%'
        for c in reversed(s):
            if c == '*':
                length += 1
            elif c == '#':
                if k + 1 > (length + 1) // 2:   # k lies in 2nd half
                    k -= length // 2
                length = (length + 1) // 2
            elif c == '%':
                k = length - k - 1
            else:
                if k + 1 == length:
                    return c
                length -= 1
        return '.'

