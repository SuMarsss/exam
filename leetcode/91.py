# date： 2020年6月12日
# methode： dp
# starting time： 3.11PM
# termina time：

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        dp = [0] * len(s)
        if int(s[0]) == 0:
            return 0
        dp[0] = 1
        pre = 1
        for i in range(1,len(s)):
            if int(s[i]) and int(s[i-1:i+1]) <= 26:
                dp[i] = dp[i-1] + pre
                pre = dp[i-1]
            else:
                dp[i] = dp[i-1]
                pre = dp[i-1]
        return dp[-1]
s = "2022"
ans = Solution().numDecodings(s)
