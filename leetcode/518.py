class Solution:
    def change(self, amount: int, coins):
        size = len(coins)-1
        def dfs(num, tot):
            if tot == 0:
                return 1
            if num <0:
                return 0

            if tot <0:
                return 0
            # 选
            Choose = dfs(num, tot-coins[num])
            # 不选
            Skip = dfs(num-1, tot)
            return Choose + Skip
        return dfs(size, amount)

amount = 0
coins = []
ans = Solution().change(amount, coins)

amount = 500
coins = [3,5,7,8,9,10,11]
ans = Solution().change(amount, coins)