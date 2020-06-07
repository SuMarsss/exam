"""
# date:  2020年6月7日
# method: dp
"""
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

nums = [2,7,9,3,1]
ans = rob(nums)