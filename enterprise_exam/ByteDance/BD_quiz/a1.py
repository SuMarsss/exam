# coding=utf-8
import sys
# 找出第k大的数

# str = input()
# print(str)
def quick_sort(nums):
    size = len(nums)
    l, r = 0, size - 1
    p = l
    r_Flag = 1
    while l < r:
        if r_Flag:
            if nums[r] > nums[l]:
                r -= 1
            elif nums[r] < nums[l]:
                nums[r], nums[l] = nums[l], nums[r]
                p = r
                l += 1
                r_Flag = 0
        else:
            if nums[l] < nums[r]:
                l += 1
            elif nums[l] > nums[r]:
                nums[r], nums[l] = nums[l], nums[r]
                p = l
                r -= 1
                r_Flag = 1
    return (nums, p)


def sort_k(nums, p=-1):
    if len(nums) == 1:
        return nums
    left,p1 =quick_sort(nums[:p])
    right,p2 = quick_sort(nums[p+1:])
    sort_k(left,p1)
    sort_k(right,p2)
    return nums


nums =[3,9,10,2,7]
k=2
quick_sort(nums)
ans = sort_k(nums)


