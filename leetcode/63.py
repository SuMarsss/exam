class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        row_len = len(obstacleGrid)
        col_len = len(obstacleGrid[0])

        # if obstacleGrid[-1][-1] == 1:
        #     return 0
        # if row_len == 1:
        #     if 1 in obstacleGrid[0]:
        #         return 0
        #     else:
        #         return 1
        # if col_len == 1:
        #     for i in range(row_len):
        #         if obstacleGrid[i][0] == 1:
        #             return 0
        #     return 1
        dp = [[0] * col_len for i in range(row_len)]
        col_flag = 0
        for j in range(col_len):
            if obstacleGrid[0][j] == 0 and col_flag == 0:
                dp[0][j] = 1
            else:
                dp[0][j],col_flag = 0,1

        row_flag = 0
        for i in range(row_len):
            if obstacleGrid[i][0] == 0 and row_flag == 0:
                dp[i][0] = 1
            else:
                dp[i][0],row_flag = 0,1



        for i in range(1, row_len):
            for j in range(1, col_len):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]


obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
ans = Solution().uniquePathsWithObstacles(obstacleGrid)
