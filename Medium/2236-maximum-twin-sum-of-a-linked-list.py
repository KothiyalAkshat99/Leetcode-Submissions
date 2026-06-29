"""
Problem Name: Maximum Twin Sum of a Linked List
Difficulty: Medium
Tags: Linked List, Two Pointers, Stack
"""

"""
Submission 1
Language: python3
Runtime: 52 ms
Memory: 62.5 MB
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        half = []
        slow = head
        fast = head

        while fast and fast.next:
            half.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        
        ret = 0
        while slow:
            ret = max(ret, half.pop() + slow.val)
            slow = slow.next
        
        return ret

