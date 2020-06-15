class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        from  collections import deque
        st_i = 0
        q = deque()
        q.append(st_i)
        past = set()
        while q:
            st_i = q.popleft()
            for word in wordDict:
                size = len(word)
                if s[st_i:size+st_i] ==word and size + st_i not in past:
                    q.append( size + st_i)
                    past.add( size + st_i)
            if st_i == len(s):
                return True
        return False


s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]
ans = Solution().wordBreak(s, wordDict)

