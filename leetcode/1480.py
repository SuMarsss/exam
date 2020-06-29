class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        size = len(nums)
        dp = [0] * size
        dp[0] = nums[0]
        for i in range(1,size):
            dp[i] = dp[i-1] +nums[i]
        return dp

nums = [1,2,3,4]
ans = Solution().runningSum(nums)
