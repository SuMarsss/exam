class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s_q = list(s)
        p_q = []
        tmp = ""
        for i in range(len(p)):
            if p[i] == "*":
                p_q.append((tmp, p[i]))
                tmp = ""
            elif p[i] == ".":
                p_q.append(("", p[i]))
                p_q.append((tmp, False))
                tmp = ""
            else:
                tmp += p[i]
                if i == len(p) -1 :
                    p_q.append((tmp, False))

        while s:
            p_pop = p_q.pop()
            if not p_pop[1]:
                if s[-len(p_pop[0]):] != p_pop[0]:
                    return  False
                else:
                    s = s[:-len(p_pop[0])]
            elif p_pop[1] == "*":
                while s[-len(p_pop[0]):] == p_pop[0]:
                    s = s[:-len(p_pop[0])]



s = "aab"
p = "c*a*b"
ans = Solution().isMatch(s,p)


