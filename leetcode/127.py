class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        memo = {}
        def change(s,t):
                if len(s) != len(t):
                    return False
                cnt = 0
                for i in range(len(s)):
                    if s[i] != t[i]: cnt +=1
                return True if cnt == 1 else False

        from collections import deque
        q = deque()
        q.append((beginWord,1))
        word_set = set(wordList)
        while q:
            cur,level = q.popleft()
            word_list = list(cur)
            for j in range(len(beginWord)):
                origin_char = word_list[j]

                for k in range(26):
                    word_list[j] = chr(ord('a') + k)
                    word = ''.join(word_list)
                    if word == cur:
                        continue

                    if word in memo: continue
                    elif word in word_set :
                        if word == endWord:
                            print(memo)
                            return level + 1
                        q.append((word,level+1))
                        memo[word] = level +1
                word_list[j] = origin_char

        print(memo)
        return 0


beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

ans = Solution().ladderLength(beginWord,endWord,wordList)






