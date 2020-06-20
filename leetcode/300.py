class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        size = len(nums)
        dp = [1] * size
        ans = 1
        for i in range(1,size):
            for j in range(i+1):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
                    ans = max(dp[i], ans)
        return ans

nums =  [10,9,2,5,3,7,101,18]
ans = Solution().lengthOfLIS(nums)