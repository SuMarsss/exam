# date: 2020年6月8日
# Strating time： 3.46PM
# terminal time：
# method： stack
# stack 先存前缀 再存下一层的倍数
class Solution:
    def decodeString(self, s: str) -> str:
        def dfs(s,i):
            res, multi = "", 0
            while i < len(s):
                ch = s[i]
                if "0"<=ch<="9":
                    multi = multi *10 + int(ch)
                elif ch == "[":
                    nxt_res,i = dfs(s, i + 1)
                    res += multi * nxt_res
                    multi = 0
                elif ch == "]":
                    return (res,i)
                else:
                    res += ch
                i += 1
            return res
        return dfs(s,0)


s = "3[a]2[bc]"
ans = Solution().decodeString(s)