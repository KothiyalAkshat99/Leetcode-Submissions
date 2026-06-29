"""
Problem Name: Valid Parenthesis String
Difficulty: Medium
Tags: String, Dynamic Programming, Stack, Greedy
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 17.7 MB
"""
class Solution:
    def checkValidString(self, s: str) -> bool:
        stk = []
        ast = []

        for i in range(len(s)):
            c = s[i]
            if c == "(":
                stk.append(i)
            elif c == "*":
                ast.append(i)
            else:
                if stk:
                    stk.pop()
                elif ast:
                    ast.pop()
                else:
                    return False
        
        while stk and ast:
            # if remaining asterisk is before remaining OPEN bracket
            if stk.pop() > ast.pop():
                return False
        
        return not stk

"""
Submission 2
Language: python3
Runtime: 0 ms
Memory: 19.4 MB
"""
class Solution:
    def checkValidString(self, s: str) -> bool:
        par_left = []
        ast = []

        for i, char in enumerate(s):
            if char == '(':
                par_left.append(i)
            elif char == '*':
                ast.append(i)
            else:
                if par_left:
                    par_left.pop()
                elif ast:
                    ast.pop()
                else:
                    return False
            
        while par_left and ast:
            if par_left.pop() > ast.pop():  # If ast comes before '('
                return False

        return False if par_left else True

