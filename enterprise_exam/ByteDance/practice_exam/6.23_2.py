class Solution:
    def change(self, amount: int, coins):
        size = len(coins)-1
        def dfs(num, tot,rest):
            res = []
            if tot == 0:
                return rest
            if num <0 or tot<0:
                return []
            # 选
            Choose = dfs(num, tot-coins[num],rest+[coins[num]])
            # 不选
            Skip = dfs(num-1, tot,rest)
            if Choose:
                if type(Choose[0]) == list:
                    res += Choose
                else:
                    res.append(Choose)
            if Skip:
                if type(Skip[0]) == list:
                    res += Skip
                else:
                    res.append(Skip)
            return res
        return dfs(size, amount, [])

amount = 500
coins = [3,5,7,8,9,10,11]
ans = Solution().change(amount, coins)