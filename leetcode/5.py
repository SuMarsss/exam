# date: 2020年6月10日
class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_len = len(s)
        if not s:
            return s
        dp = [[False]*s_len for i in range(s_len)]
        st_i, maxLen = 0, 0
        ans = ""
        for j in range(s_len):
            for i in range(0, j):
                if s[j] == s[i]:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                if dp[i][j]:
                    tLen = j - i +1
                    if tLen > maxLen:
                        ans = s[i:j+1]
                        maxLen = tLen
        if not ans:
            return s[0]
        return ans


s = "abcda"
ans = Solution().longestPalindrome(s)