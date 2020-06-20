class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        dp = [0] *size
        dp[0] = nums[0]
        ans = dp[0]
        for i in range(1,size):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
            ans = max(dp[i], ans)
        return ans

nums = [-2,1,-3,4,-1,2,1,-5,4]
ans = Solution().maxSubArray(nums)