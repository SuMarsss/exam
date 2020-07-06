class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def _sort(nums, low, high):
            l, r = low, high
            p = l
            while l < r:
                if l < r:
                    while nums[r] < nums[p]:
                        r -= 1
                    nums[r], nums[p] = nums[p], nums[r]
                    p = r
                    l += 1
                if l < r:
                    while nums[l] > nums[p]:
                        l += 1
                    nums[l], nums[p] = nums[p], nums[l]
                    p = l
                    r -= 1
            return p


        def quick_sort(nums, low, high):
            if low >= high:
                return

            p = _sort(nums, low, high)
            quick_sort(nums, low, p - 1)
            quick_sort(nums, p+1, high)



        low, high = 0, len(nums) - 1
        left = 0
        right = len(nums) - 1
        k = 2
        while 1:
            idx = _sort(nums, left, right)
            if idx == k - 1:
                return nums[idx]
            if idx < k - 1:
                left = idx + 1
            if idx > k - 1:
                right = idx - 1

        return nums


nums = [5, 3, 7, 9, 4]
Solution().sortArray(nums)