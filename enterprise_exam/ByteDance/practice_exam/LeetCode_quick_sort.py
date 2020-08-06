class Solution:
    def randomized_partition(self, nums, l, r):
        # pivot = l
        # nums[pivot], nums[r] = nums[r], nums[pivot]
        i = l - 1
        for j in range(l, r):
            if nums[j] < nums[r]:
                i += 1
                nums[j], nums[i] = nums[i], nums[j]
        i += 1
        nums[i], nums[r] = nums[r], nums[i]
        return i

    def randomized_quicksort(self, nums, l, r):
        if r - l <= 0:
            return
        mid = self.randomized_partition(nums, l, r)
        self.randomized_quicksort(nums, l, mid - 1)
        self.randomized_quicksort(nums, mid + 1, r)

    def sortArray(self, nums) :
        self.randomized_quicksort(nums, 0, len(nums) - 1)
        return nums

nums =[5,2,3,1]
# Solution().sortArray(nums)


def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    base = nums[0]

    L, R = [], []
    for i in nums[1:]:
        if i < base:
            L.append(i)
        else:
            R.append(i)
    return quick_sort(L) + [base] + quick_sort(R)

ans = quick_sort(nums)