# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum: int) :
        res = []
        if not root:
            return res

        def dfs(node, pre_sum, li):

            if not node.left and not node.right:
                if pre_sum + node.val == sum:
                    res.append(li + [node.val])
            if node.left:
                dfs(node.left, pre_sum + node.val, li + [node.val])
            if node.right:
                dfs(node.right, pre_sum + node.val, li + [node.val])

        dfs(root, 0, [])
        return res