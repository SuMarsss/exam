"""
date： 2020年6月18日21:56:47
"""


class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        if not matrix: return ans
        row_len = len(matrix)
        col_len = len(matrix[0])
        i, j = 0, 0
        up_flag = 1
        ans.append(matrix[i][j])
        while not (i == row_len - 1 and j == col_len - 1):
            if up_flag:
                nxt_i, nxt_j = i-1, j+1
                if 0<=nxt_i<=row_len-1 and 0<=nxt_j<=col_len-1:
                    i,j = nxt_i,nxt_j
                    ans.append(matrix[i][j])
                    continue
                else:
                    up_flag = 0
                    if 0<=j+1<=col_len-1:
                        i,j = i, j+1
                    else:
                        i,j = i+1,j
                    ans.append(matrix[i][j])
            else:
                nxt_i, nxt_j = i+1, j - 1
                if 0<=nxt_i<=row_len-1 and 0<=nxt_j<=col_len-1:
                    i,j = nxt_i,nxt_j
                    ans.append(matrix[i][j])
                    continue
                else:
                    up_flag = 1
                    if 0<=i+1<=row_len-1:
                        i,j = i+1, j
                    else:
                        i,j = i,j+1
                    ans.append(matrix[i][j])
        return ans

matrix = [[1,2,3],[4,5,6],[7,8,9]]
ans = Solution().findDiagonalOrder(matrix)
