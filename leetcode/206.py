# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head) :
        if not head:
            return []
        cur = head
        nxt = head.next
        if not nxt:
            return head
        cur.next = None
        while nxt.next:
            tmp = nxt.next
            nxt.next = cur
            cur = nxt
            nxt = tmp
        nxt.next = cur
        return nxt

