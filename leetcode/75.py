# starting time:

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        cur,p0,p2 = 0,0,n-1
        while cur <= p2 :
            if nums[cur] == 0:
                nums[cur],nums[p0] = nums[p0], nums[cur]
                p0 += 1
                cur += 1
            elif nums[cur] == 2:
                nums[cur],nums[p2] = nums[p2], nums[cur]
                p2 -= 1
            else:
                cur += 1

nums =  [2,0,1]
Solution().sortColors(nums)