#  starting time： 2020年8月2日14:51:46
# terminal time： 2020年8月2日15:46:35

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        row_len = len(board)
        col_len = len(board[0])
        # visited = [[0 for  i in range(col_len)] for j in range(row_len)]
        dir = [(0,-1),(0,1),(1,0),(-1,0)]
        for i in range(row_len):
            for j in range(col_len):
                if board[i][j] == word[0]:
                    visited = {(i,j)}
                    stack = [(i, j, word[1:], visited)]
                    while stack:
                        x,y,last, visited = stack.pop()
                        if not last:
                            return True
                        p = last[0]
                        for di, dj in dir:
                            nxt_i, nxt_j = x+di,y+dj
                            if 0<=nxt_i<row_len and 0<=nxt_j<col_len:
                                if p == board[nxt_i][nxt_j] and (nxt_i, nxt_j) not in visited:
                                    tmp = visited.copy()
                                    tmp.add((nxt_i, nxt_j))
                                    stack.append((nxt_i, nxt_j, last[1:],tmp))
        return False

board = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]

word = "ABCESEEEFS"
ans = Solution().exist(board, word)

