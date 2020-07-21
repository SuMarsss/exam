class Solution:
    def subsets(self, nums) :
        res = []
        def dfs(ind, last):
            if ind == len(nums):
                res.append(last)
                return
            else:
                dfs(ind+1, last+[nums[ind]])
                dfs(ind+1, last)
        dfs(0,[])
        return res

nums = [1,2,3]
ans = Solution().subsets(nums)