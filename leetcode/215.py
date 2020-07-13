class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def quick_sort(nums):
            size = len(nums)
            l, r = 0, size - 1
            p = l
            r_Flag = 1
            while l < r:
                if r_Flag:
                    if nums[r] >= nums[l]:
                        r -= 1
                    elif nums[r] < nums[l]:
                        nums[r], nums[l] = nums[l], nums[r]
                        p = r
                        l += 1
                        r_Flag = 0
                else:
                    if nums[l] <= nums[r]:
                        l += 1
                    elif nums[l] > nums[r]:
                        nums[r], nums[l] = nums[l], nums[r]
                        p = l
                        r -= 1
                        r_Flag = 1
            return p

        rk = len(nums) - k
        p = quick_sort(nums)
        while 1:
            if rk == p:
                return nums[p]
            if len(nums) == 1:
                return nums[0]
            elif  rk > p:
                rk -= p+1
                nums = nums[p+1:]
                p = quick_sort(nums)
            else:
                nums = nums[:p]
                p = quick_sort(nums)

nums = [3,2,3,1,2,4,5,5,6]
k = 4
ans = Solution().findKthLargest(nums,k)
