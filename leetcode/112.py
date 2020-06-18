# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum: int) :
        cur = root
        q = [(cur, 0)]
        while q:
            cur, sub_sum = q.pop()

            if sub_sum == sum:
                return True
            if cur:
                if cur.left: q.append([cur.left, cur.val+sub_sum])
                if cur.right: q.append([cur.right, cur.val+sub_sum])
        return False
