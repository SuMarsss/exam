# -*- coding: utf-8 -*-
nums = [-1,0,3,5,9,12]
target = 9
class Solution:
    def search(self, nums, target):
        numsLen = len(nums)
        p = numsLen//2
        while 1:

            if p <= 0 or p >= numsLen-1:
                return False
            if nums[p] == target:
                return p
            elif nums[p] < target:
                p += p // 2
            else:
                p -= p//2

ans = Solution().search(nums,target)
print(ans)