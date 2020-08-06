K,N = list(map(int,input().split()))
nums = list(map(int,input().split()))
# K,N = 0, 4
# nums = [6,3,3,3]
dp = [0] * N
dp[0] = K- nums[0]
ans = 0
Flag = 0
if K == 0:
    Flag = 1
    print("paradox")
else:
    ind = 0
    d = K
    cnt = 0
    while ind<N:
        d -= nums[ind]
        if d == 0:
            print("paradox")
            break
        elif d < 0:
            d = -d
            cnt += 1
        ind += 1
    if ind == N:
        print("{} {}".format(d, cnt))
