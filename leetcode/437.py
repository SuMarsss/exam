class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:

        def dfs(root, sumlist):
            if root is None:
                return 0

            sumlist = [num + root.val for num in sumlist]
            sumlist.append(root.val)

            count = 0
            for num in sumlist:
                if num == sum:
                    count += 1
            # count = sumlist.count(sum)

            return count + dfs(root.left, sumlist) + dfs(root.right, sumlist)

        return dfs(root, [])

