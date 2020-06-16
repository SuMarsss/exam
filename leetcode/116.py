"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        from collections import deque
        q = deque()
        q.append((root, 0))
        pre_level = 0
        pre = []
        while q:
            cur, level = q.popleft()
            if not cur:
                break
            q.append((cur.left, level + 1))
            q.append((cur.right, level + 1))

            if level != pre_level:
                for i in range(len(pre)-1):
                    pre[i].next = pre[i+1]
                pre_level = level
                pre = []
            else:
                pre.append(cur)


        return root
