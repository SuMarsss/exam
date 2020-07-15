class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        def dfs(cnt, cR, last):
            if cR == n and cnt ==0:
                ans.append(last)
                return None
            elif cR >n or cnt <0:
                return None
            dfs(cnt+1, cR + 1, last + "(")
            dfs(cnt-1, cR, last+")")
            return ans
        return dfs(0,0,"")
n = 3
ans = Solution().generateParenthesis(n)
