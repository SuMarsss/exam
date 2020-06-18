# date: 2020年6月18日19:20:30
#
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        visited = set()
        res = list()
        dir = [(-1,0),(0,1),(0,-1),(1,0)]
        if not board:
            return board
        row_len = len(board)
        col_len = len(board[0])
        for i in range(row_len):
            for j in range(col_len):
                if board[i][j] == "O" and (i,j) not in visited:
                    sub_res = [(i,j)]
                    q = [(i,j)]
                    visited.add((i,j))
                    boundary_Flag = 1 if i == 0 or i == row_len-1 or j==0 or j==col_len-1 else 0
                    while q:
                        cur_i, cur_j = q.pop()
                        for d_i, d_j in dir:
                            nxt_i, nxt_j = cur_i + d_i, cur_j + d_j
                            if 0<=nxt_i<=row_len-1 and 0<=nxt_j<=col_len-1:
                                if board[nxt_i][nxt_j] == "O" and (nxt_i, nxt_j) not in visited:
                                    sub_res.append((nxt_i, nxt_j))
                                    q.append((nxt_i,nxt_j))
                                    visited.add((nxt_i, nxt_j))
                                    if nxt_i == 0 or nxt_i == row_len -1 or nxt_j == 0 or nxt_j == col_len -1 :
                                        boundary_Flag = 1
                    if boundary_Flag == 0:
                        res += sub_res
        for i,j in res:
            board[i][j] = "X"


board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Solution().solve(board)
