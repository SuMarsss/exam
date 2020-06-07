class Solution:
    def removeInvalidParentheses(self, s):
        def isValid(s):
            c = 0
            for i in s:
                if i == "(":
                    c += 1
                elif i == ")":
                    c -= 1
                if c < 0:
                    break
            return c == 0

        cur_level = {s}
        while 1:
            ans = list(filter(isValid, cur_level))
            if ans:  return ans
            nxt_level = set()
            for s in cur_level:
                for i, ch in enumerate(s):
                    if ch in "()":
                        nxt_level.add(s[:i]+s[i+1:])
            cur_level = nxt_level


s = "()())()"
ans = Solution().removeInvalidParentheses(s)
