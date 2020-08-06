class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        def dfs(nums, last):
            if not nums:
                res.append(last)
            for i in range(len(nums)):
                if i>=1 and nums[i] == nums[i-1]:
                    continue
                dfs(nums[:i]+nums[i+1:], last+[nums[i]])

        dfs(nums, [])
        return res

nums = [1,1,2]
ans = Solution().permuteUnique(nums)
