class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import deque
        size = len(s)
        q = set()
        ans = 0
        left = 0
        for i in range(size):
            if not q:
                q.add(s[i])
                ans = 1
            else:
                while s[i] in q:
                    q.remove(s[left])
                    left += 1
                q.add(s[i])
                ans = max(len(q), ans)
        return ans
s = "dvdf"
ans = Solution().lengthOfLongestSubstring(s)

