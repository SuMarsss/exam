class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        stack = []
        maxLen = 0
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                if len(stack) == 0:
                    stack.append(i)
                else:
                    if s[stack.pop()] == ")":
                        stack.append(i)
                        continue
                    if len(stack) == 0:
                        maxLen = max(maxLen, i +1)
                    else:
                        maxLen = max(maxLen, i - stack[-1])
        return maxLen

s =  ")()())()()("
ans = Solution().longestValidParentheses(s)
