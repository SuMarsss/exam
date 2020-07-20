# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        h = set()
        cur = headA
        while cur:
            h.add(cur)
            cur = cur.next
        cur = headB
        while cur:
            if cur in h:
                return cur
            cur = cur.next
        return None