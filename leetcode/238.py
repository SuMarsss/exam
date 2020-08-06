class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        size = len(nums)
        L,R = [1]* size,[1]* size
        res = []
        for i in  range(1, size):
            L[i] = L[i-1] * nums[i-1]
            R[size-1-i] = R[size-i] * nums[size-i]
        for i in range(size):
            res.append(L[i]*R[i])
        return res

nums = [1,2,3,4]
ans = Solution().productExceptSelf(nums)