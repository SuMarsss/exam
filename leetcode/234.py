# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        from collections import deque
        q = deque()
        cur = head
        while cur:
            q.append(cur.val)
            cur = cur.next
        print(q)
        while q:
            if len(q) == 1:
                return  True
            l,r = q.popleft(), q.pop()
            if l != r:
                return False
        return True