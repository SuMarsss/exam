class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int] 消耗
        :type s: List[int]  资源
        :rtype: int
        """

        lg = len(g)
        ls = len(s)
        i_g,i_s = 0,0
        g.sort()
        s.sort()
        ans = 0
        while i_g<=lg-1 and i_s<=ls-1:
            if g[i_g] <= s[i_s]:
                i_g += 1
                i_s += 1
                ans += 1
            else:
                i_s += 1
        return ans

g= [1,2,3]
s = [1,1]
ans = Solution().findContentChildren(g,s)

