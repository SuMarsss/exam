# starting time: 2020年7月23日14:37:36
# end time: 2020年7月23日15:00:09
# method 1: heapq
from heapq import *


class Solution:
    def getLeastNumbers(self, arr, k):

        q = []
        size = len(arr)
        if k == 0:
            return []
        for i in range(k):
            heappush(q, -arr[i])
        for i in range(k, size):
            if arr[i] < -q[0]:
                heapreplace(q, -arr[i])
        return [-i for i in q]

arr = [3,2,1]
k = 2
ans = Solution().getLeastNumbers(arr,k)