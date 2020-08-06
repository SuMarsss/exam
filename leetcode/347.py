class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import Counter
        import heapq
        dic = Counter(nums)
        queue, res = [], []
        for i in dic:
            heapq.heappush(queue, (-dic[i], i))
        for i in range(k):
            tmp = heapq.heappop(queue)
            res.append(tmp[1])
        return res
nums = [1,1,1,2,2,3]
k = 2
ans = Solution().topKFrequent(nums, k)
