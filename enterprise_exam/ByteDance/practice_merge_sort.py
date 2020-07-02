def merge(nums1, nums2):
    len1, len2 = len(nums1), len(nums2)
    min_len = min(len1, len2)
    x = list()
    i,j = 0,0
    ans = []
    while i < len1 and j < len2:
        if nums1[i] > nums2[j]:
            ans.append(nums2[j])
            j += 1
        else:
            ans.append(nums1[i])
            i += 1
    if i == len1:
        ans += nums2[j:]
    elif j == len2:
        ans += nums1[i:]
    return ans

def merge_sort(nums):
    if len(nums) == 1:
        return nums
    middle = len(nums) // 2
    left = merge_sort(nums[:middle])
    right = merge_sort(nums[middle:])
    return merge(left, right)
nums1 = [1, 3, 7, 9]
nums2 = [2, 4, 5, 6]
nums = nums1 + nums2
ans = merge_sort(nums)