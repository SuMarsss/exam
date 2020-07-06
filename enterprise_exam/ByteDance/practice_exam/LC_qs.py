def quick_sort(nums):
    n = len(nums)
    if n <= 1:
        return nums
    left,right = [], []
    p = nums[0]
    for i in range(1,n):
        if nums[i] > p :
            right.append(nums[i])
        else:
            left.append(nums[i])
    return quick_sort(left) + [p] + quick_sort(right)


nums =[5,2,3,1]
ans = quick_sort(nums)