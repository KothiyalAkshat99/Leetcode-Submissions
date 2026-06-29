"""
Problem Name: Delete the Middle Node of a Linked List
Difficulty: Medium
Tags: Linked List, Two Pointers
"""

"""
Submission 1
Language: python3
Runtime: 64 ms
Memory: 48.4 MB
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        
        dummy = None
        slow = head
        fast = head

        while fast and fast.next:
            dummy = slow
            slow = slow.next
            fast = fast.next.next
        
        dummy.next = slow.next
        slow.next = None
        slow = None

        return head

"""
Submission 2
Language: python3
Runtime: 71 ms
Memory: 62.4 MB
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        
        prev = None
        slow, fast = head, head
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        prev.next = slow.next
        slow.next = None
        slow = None

        return head

