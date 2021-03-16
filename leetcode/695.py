class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        from collections import  deque

        if not grid:
            return 0
        col_nums = len(grid[0])
        row_nums = len(grid)
        visited = [[False for i in range(col_nums)] for j in range(row_nums)]
        maxArea = 0
        dirs = [(0,-1),(-1,0),(0,1),(1,0)]
        for i in range(row_nums):
            for j in range(col_nums):
                if not visited[i][j] and grid[i][j]:
                    visited[i][j] = 1
                    q = deque([(i,j)])
                    curArea = 1
                    while q:
                        cur_i, cur_j = q.popleft()
                        for d in dirs:
                            nxt_i, nxt_j = cur_i + d[0], cur_j + d[1]
                            if 0 <= nxt_i < row_nums and 0 <= nxt_j < col_nums:
                                if not visited[nxt_i][nxt_j] and grid[nxt_i][nxt_j]:
                                    visited[nxt_i][nxt_j] = 1
                                    q.append((nxt_i, nxt_j))
                                    curArea += 1
                    maxArea = max(maxArea, curArea)
        return maxArea

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]

ans = Solution().maxAreaOfIsland(grid)