class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        zero_p = -1
        for i in range(size):
            if zero_p == -1:
                if nums[i] == 0:
                    zero_p = i
            else:
                if nums[i] != 0:
                    nums[i], nums[zero_p] = nums[zero_p], nums[i]
                    zero_p += 1
        return nums

nums = [0,1,0,3,12]
ans = Solution().moveZeroes(nums)