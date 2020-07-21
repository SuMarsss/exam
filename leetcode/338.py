class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        size = num + 1
        dp = [0] * size
        dp[0] = 0
        for i in range(size):
            if i % 2 == 1:
                dp[i] = dp[i-1] +1
            elif i % 2 == 0:
                dp[i] = dp[i // 2]
        return dp
num = 10
ans = Solution().countBits(num)
