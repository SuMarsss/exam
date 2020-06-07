"""
date: 2020年6月7日
method： BFS + 递归
"""
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root):
            if not root:
                return (0,0)
            if root.left in root_dict:
                robL, skipL = root_dict[root.left]
            else:
                robL, skipL = dfs(root.left)
            if root.right in root_dict:
                robR, skipR = root_dict[root.right]
            else:
                robR, skipR = dfs(root.right)
            robN = root.val + skipL + skipR
            skipN = max(skipL, robL) + max(skipR, robR)
            return (robN,skipN)

        root_dict = {}
        return max(dfs(root))