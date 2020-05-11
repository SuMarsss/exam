# -*- coding: utf-8 -*-

class Solution:
    def canJump(self, nums):
        if not nums:
            return False
        N = len(nums)
        if N == 1:
            return True
        cur = 0
        while 1:            
            cur_val = nums[cur]
            nxt_range = cur_val

            max_nxt = 0
            best = 0     
            for i, val in enumerate(nums[cur+1:cur+nxt_range+1]):
                if i+val+cur+1 >= max_nxt:
                    max_nxt =  i+val+cur+1
                    best = i+cur+1
            cur = best
            if cur >= N-1:
                return True
            elif nums[cur] == 0:
                return False
            
ex = [2,0,0]    
ans = Solution().canJump(ex)     
print(ans) 