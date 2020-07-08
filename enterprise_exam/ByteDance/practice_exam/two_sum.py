def twoSum( nums, target):
    size = len(nums)
    ha = set()
    ans = []
    vis = set()
    for i in range(size):
        if target - nums[i] in ha:
            if target - nums[i] not in vis:
                ans.append([target - nums[i], nums[i]])
                vis.add(target - nums[i])
                vis.add(nums[i])

        else:
            ha.add(nums[i])
    return ans

nums = [2,7,11,15,1,8,2,7]
target = 9
ans = twoSum(nums, target)