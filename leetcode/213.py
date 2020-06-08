class Solution:
    def rob(self, nums) :
        def rob(nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            dp = [0] * len(nums)
            if not nums:
                return 0
            if len(nums) <= 2:
                return max(nums)
            dp[0], dp[1] = nums[0], nums[1]
            mmax = max(dp[0], dp[1])
            for i in range(2, len(nums)):
                preMax = max(dp[i - 2], dp[i - 3])
                dp[i] = preMax + nums[i]
                mmax = max(mmax, dp[i])
            return mmax

        return  max(rob(nums[:-1]),rob(nums[1:])) if len(nums) >1 else nums[0]

nums=[1,2,3,1]
ans = Solution().rob(nums)