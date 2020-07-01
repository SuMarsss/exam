class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        size = len(candidates) -1
        candidates.sort()
        min_num = candidates[0]
        def dfs(num, tot, last):
            res = []
            if tot == 0:
                return last
            else:
                if min_num> tot:
                    return []
            if num < 0:
                return []
            ChN = dfs(num, tot-candidates[num], last+[candidates[num]])
            SkN = dfs(num-1, tot, last)
            if ChN:
                if type(ChN[0]) == int:
                    res.append(ChN)
                else:
                    res += ChN
            if SkN:
                if type(SkN) == int:
                    res.append(SkN)
                else:
                    res += SkN
            return res
        return dfs(size, target, [])



candidates = [2]
target = 1
ans = Solution().combinationSum(candidates, target)