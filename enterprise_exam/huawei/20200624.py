def res(nums):
    size = len(nums)
    ans = set()
    for i in range(size):
        for j in range(size):
            if j == i: continue
            for k in range(size):
                if k == j or k == i: continue
                res = 100 * nums[i] + 10 * nums[j] + nums[k]
                ans.add(res)
    return ans

nums = [1,2,3,4]
ans = res(nums)