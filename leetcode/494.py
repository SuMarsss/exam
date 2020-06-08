class Solution:
    def findTargetSumWays(self, nums, S: int) -> int:
        sum_nums = sum(nums)
        if len(nums) == 1:
            return 1 if nums[0] == S or nums[0] == -S  else 0
        dp = [[0 for i in range(sum_nums*2+1)] for j in range(len(nums))]
        if nums[0] == 0:
            dp[0][sum_nums - nums[0]] = 2
        else:
            dp[0][sum_nums-nums[0]], dp[0][sum_nums+nums[0]] = 1,1
        for i in range(1,len(nums)):
            for j, _ in enumerate(dp[0]):

                sub_res = dp[i-1][j - nums[i]] if j - nums[i] >=0 else 0
                add_res = dp[i-1][j + nums[i]] if j + nums[i] <len(dp[0]) else 0
                dp[i][j] = sub_res+ add_res
        print(dp)
        return dp[-1][S+sum_nums] if S+sum_nums<len(dp[0]) and S+sum_nums>-1 else 0


s = [0,0,0,0,0,0,0,0,1]
ans = Solution().findTargetSumWays(s, 1)
