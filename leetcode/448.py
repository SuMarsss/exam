class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        if not nums:
            return res
        from collections import defaultdict
        d = defaultdict(int)
        maxNum = 1
        freqNum = 1
        for num in nums:
            # if num in d:
            #     freqNum += 1
            d[num] += 1
            maxNum = max(maxNum, num)
        maxNum = max(maxNum, len(nums))

        for i in range(1, maxNum+1):
            if i not in d:
                res.append(i)
        return res

nums = [1,1,2,2]
ans = Solution().findDisappearedNumbers(nums)