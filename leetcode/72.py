class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        row_len, col_len = len(word1), len(word2)
        dp = [[-1 for i in range(col_len + 1)] for j in range(row_len + 1)]
        for i in range(row_len+1):
            dp[i][0] = i
        for j in range(col_len+1):
            dp[0][j] = j
        def dfs(i, j):
            if dp[i][j] != -1:
                return dp[i][j]
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dfs(i-1,j-1)
            else:
                dp[i][j] = min(dfs(i, j - 1) + 1, dfs(i - 1, j) + 1, dfs(i - 1, j - 1) + 1)
            return dp[i][j]
        return dfs(row_len, col_len)


word1 = "horse"
word2 = "ros"
ans = Solution().minDistance(word1, word2)
