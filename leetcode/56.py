class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []
        num = len(intervals)
        intervals.sort(key=lambda x:x[0])
        ans = []
        cur = intervals[0]
        i = 1
        while i < num:
            if cur[1] >= intervals[i][0]:
                # cur[0] =  min(cur[0])intervals[i][0]
                cur[1] = max(cur[1], intervals[i][1])
                i += 1
            else:
                ans.append(cur)
                cur = intervals[i]
                i += 1
        ans.append(cur)
        return ans

intv = [[1,3],[2,6],[8,10],[15,18]]
ans = Solution().merge(intv)