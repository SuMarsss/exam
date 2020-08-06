N = int(input())
nums = []
minN, maxN = 1e9, 0
for _ in range(N):
    S, E = list(map(int,input().split()))
    nums.append([S,E])
    minN = min(minN,S)
    maxN = max(maxN, E)

dp = [0 for i in range(minN, maxN+1)]
# nums.sort()a
ans = 0
for s,e in nums:
    # for i in range(s-minN+1, e-minN+1):
    #     dp[i] += 1
    dp[s-minN+1:e-minN+1] = [i+1 for i in dp[s-minN+1:e-minN+1] ]
print(max(dp))

