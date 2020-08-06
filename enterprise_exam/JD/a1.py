N = int(input())
text1 = input().split()
text2 = input().split()
n = m = N
# 构建 DP table 和 base case
dp = [[0] * (n + 1) for _ in range(2)]
# 进行状态转移
for i in range(1, m + 1):
    for j in range(1, n + 1):
        if text1[i - 1] == text2[j - 1]:
            # 找到一个 lcs 中的字符
            dp[1][j] = 1 + dp[0][j - 1]
        else:
            dp[1][j] = max(dp[0][j], dp[1][j - 1])
    dp[0] = dp[1].copy()
res = dp[-1][-1]
rate = res/N
rate  = round(rate*100)/100.0
if rate<=0.5:
    print("{:.2} Yes".format(rate))
else:
    print("{:.2} No".format(rate))
