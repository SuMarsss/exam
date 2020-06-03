nums = [-1, 0, 1, 2, -1, -4]
ans = list()
numsLen = len(nums)
nums.sort()
for i in range(numsLen):
    if i > numsLen - 3:
        break
    if nums[i] > 0:
        break

    if i :
        if nums[i] == nums[i-1]:
            continue
    l = i + 1
    r = numsLen - 1

    while l < r:
        sumNums = nums[i] + nums[l] + nums[r]
        if sumNums < 0:
            l += 1
        elif sumNums > 0:
            r -= 1
        else:
            ans.append([nums[i], nums[l], nums[r]])
            l += 1
            r -= 1

ans = list(ans)