# class Solution(object):
#     def coinChange(self, coins, amount):
#         memo = {}
#         def dfs(n):
#             if n == 0: return 0
#             if n < 0: return -1
#             if n in memo: return memo[n]
#             res = float("inf")
#             for coin in coins:
#                 rest_min = dfs(n - coin) + 1
#                 if rest_min >0:
#                     res = min(res, rest_min)
#             memo[n] = res
#             return res if res != float("inf") else -1
#         return dfs(amount)

# methond2: DP
class Solution(object):
    def coinChange(self, coins, amount):
        dp = [float("inf")] * (amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i-coin] + 1, dp[i])
        return dp[-1] if dp[-1] != float("inf") else -1
# coins = [186,419,83,408]
# amount = 6249
coins = [1,2,5]
amount = 11
ans = Solution().coinChange(coins, amount)
