# 876. Middle of the Linked List
# https://leetcode.com/problems/middle-of-the-linked-list/description/
# Beats: 100.00% [Solved as from solutions]
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
