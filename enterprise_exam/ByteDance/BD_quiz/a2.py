#coding=utf-8
import sys
#str = input()
#print(str)
print('Hello,World!')
def find_freq(nums):
    size = len(nums)
    ha = dict()
    for i in range(size):
        if nums[i] in ha:
            ha[nums[i]] += 1
            if ha[nums[i]] >= size//2:
                return nums[i]
        else:
            ha[nums[i]] = 0

nums = list(map(int,input().split()))
ans = find_freq(nums)
print(ans)