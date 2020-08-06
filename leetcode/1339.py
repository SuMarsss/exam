# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxProduct(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        visited = {}
        def sum_node(root):
            if not root:
                return 0
            if root in visited:
                return visited[root]
            l = sum_node(root.left)
            r = sum_node(root.right)
            sub_res = root.val + l+ r
            visited[root] = sub_res
            # maxProduct = max(maxProduct, sub_res-l, sub_res-r)
            return sub_res

        def dfs(root):
            maxProduct = 0
            if not root:
                return 0
            stack = [root]
            while stack:
                node = stack.pop()
                if node.left:
                    stack.append(node.left)
                    maxProduct = max(maxProduct, (sum_node(root) - sum_node(node.left))*sum_node(node.left))
                if node.right:
                    stack.append(node.right)
                    maxProduct = max(maxProduct, (sum_node(root) - sum_node(node.right))*sum_node(node.right))
            return maxProduct % (10**9 + 7 )

        return  dfs(root)