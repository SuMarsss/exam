# 二分查找
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        row_len = len(matrix)
        col_len = len(matrix[0])
        for i in range(row_len):
            if not matrix[i]: continue
            if matrix[i][0] <= target <= matrix[i][-1]:
                l,r=0,col_len-1
                while l <= r:
                    mid = (l +r) // 2
                    if matrix[i][mid] < target:
                        l = mid + 1
                    elif matrix[i][mid] > target:
                        r = mid - 1
                    elif matrix[i][mid] == target:
                        return True
        return False


matrix = [[-1,3,4]]

target = -1

ans = Solution().searchMatrix(matrix, target)

