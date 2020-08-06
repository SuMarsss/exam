class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        size = len(s)
        dp = [[False for i in range(size)] for j in range(size)]
        res = 0
        for i in range(size):
            for j in range(i + 1):
                if i == j:
                    dp[i][j] = True
                else:
                    if s[i] == s[j]:
                        dp[i][j] = dp[i - 1][j + 1] if i > j + 1 else True
                if dp[i][j]:
                    res += 1
        return res

s = "cabad"
ans = Solution().countSubstrings(s)