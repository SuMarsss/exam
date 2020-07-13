class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        col_len = len(grid[0])
        row_len = len(grid)
        scores = [[0]*col_len for i in range(row_len)]
        scores[0][0] = grid[0][0]
        for i in range(1,row_len):
            scores[i][0] = scores[i-1][0] + grid[i][0]
        for j in range(1, col_len):
            scores[0][j] = scores[0][j-1] + grid[0][j]
        for i in range(1, row_len):
            for j in range(1, col_len):
                scores[i][j] = grid[i][j] + min(scores[i][j-1], scores[i-1][j])
        return scores[-1][-1]

grid = [[1,2,5],[3,2,1]]
ans = Solution().minPathSum(grid)