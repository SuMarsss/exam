class Solution:
    def permute(self, nums) :
        res = []
        def dfs(nums, last):
            if not nums:
                return res.append(last)
            for i in range(len(nums)):
                dfs(nums[:i]+nums[i+1:], last+[nums[i]])
        dfs(nums, [])
        return res

nums = [1,2,3]
ans = Solution().permute(nums)

""" [1,2,3]
[
    [1,2,3],
    [1,3,2],
]

"""
