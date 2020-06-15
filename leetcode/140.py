class Solution:
    def wordBreak(self, s, wordDict):
        memo = {}

        def dfs(s):
            if not s:
                return ""
            if s in memo:
                return memo[s]
            res = []
            for word in wordDict:
                if s.startswith(word):
                    if len(word) == len(s):
                        res.append(word)
                    else:
                        rest = dfs(s[len(word):])
                        for item in rest:
                            item = word + " " + item
                            res.append(item)
            memo[s] = res
            return res

        return dfs(s)


s = "aaaa"
wordDict = ["a", "aa", "aaa"]

ans = Solution().wordBreak(s, wordDict)
