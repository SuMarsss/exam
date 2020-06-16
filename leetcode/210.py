# outdegree 0

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        nums = numCourses
        outdegrees = [0] * numCourses
        adj = [[]  for _ in range(numCourses)]
        for nxt, cur in prerequisites:
            outdegrees[nxt] += 1
            adj[cur].append(nxt)
        outs_0 = []
        for i in range(numCourses):
            if outdegrees[i] == 0:
                outs_0.append(i)
                numCourses -= 1
        res = outs_0.copy()
        while outs_0:
            outs_nxt = []
            for o in outs_0:
                for nxt in adj[o]:
                    outdegrees[nxt] -= 1
                    if outdegrees[nxt] == 0:
                        outs_nxt.append(nxt)
                        numCourses -= 1
            # if not outs_nxt:
            #     return res
            outs_0 = outs_nxt
            res += outs_0
        return res if len(res) == nums else []



numCourses = 2
prerequisites = [[1,0]]
ans = Solution().findOrder(numCourses,prerequisites)