class Solution:
    def isValid(self, s):
        dic = {'{': '}',  '[': ']', '(': ')'}
        stack = []
        for c in s:
            if c in dic: stack.append(c)
            elif len(stack)<=0 :
                return False
            elif dic[stack.pop()] != c:
                return False
        return len(stack) == 0

s = ")"
ans = Solution().isValid(s)


