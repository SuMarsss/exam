class Solution:
    def nextPermutation(self, nums) :
        """
        Do not return anything, modify nums in-place instead.
        答题思路：从后往前寻找第一个升序对(i,j)即nums[i]<nums[j] 再从后往前找第一个大于nums[i]的数即为大数，交换着两个元素即将大数换到前面，然后将大数后面的部分倒序
        """
        n = len(nums)
        for i in range(n-1, 0, -1):
            if nums[i-1] < nums[i]:
                break
        else:
            return nums.reverse()
        for j in range(n - 1, i - 1, -1):
            if nums[j] > nums[i - 1]:
                break
        nums[i-1], nums[j] = nums[j], nums[i-1]
        tmp = nums[i:]
        tmp.reverse()
        nums[i:] = tmp
        return nums