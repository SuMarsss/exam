# T = int(input())
# # T =1
# for t in range(T):
#     n,k = list(map(int, input().split()))
#     h = list(map(int, input().split()))
#
#     # n,k = [10,5]
#     # h = "50590387 8028493 660013516 226575217 85137277 569716449 31075276 331696 27381455 503700401"
#     # h = list(map(int,h.split()))
#     # n,k = [5,3]
#     # h = "6 2 4 3 8"
#     # h = list(map(int, h.split()))
#
#     if n != len(h):
#         print("len not equal")
#     HFlag = 0 # 超能力标志位，未使用为0，使用后置1
#     slist = [(0, HFlag)]
#     FindFlag = 0# 结果标志位，0输出NO，1输出YES
#     count = 0
#     while slist and not FindFlag: # slist栈不为空，一直循环
#         i,HFlag = slist.pop(0) # 出栈
#         count += 1
#         # if count > 1000000000:
#         #     print("time out")
#         #     break
#         mmax, Hmax = 0 , 0
#         for j in range(min(i+k,n-1),i,-1):# 从当前位置遍历到k个可能位置
#             # if j>=n: # 如果重复 或者超限
#             #     continue
#             if h[j]> h[i] and h[j]>Hmax and HFlag == 0: # 使用超能力找到最后一个位置 返回YES
#                 if j == n-1:
#                     FindFlag = 1
#                     print("YES")
#                     break
#                 Hmax = h[j]
#                 slist.append((j, HFlag+1))
#             elif h[j]<= h[i] and h[j]>mmax: # 小于等于 可跳
#                 mmax = h[j]
#                 slist.append((j, HFlag)) # 入栈
#                 if j == n-1: # 找到最后一个位置 返回YES
#                     FindFlag = 1
#                     print("YES")
#                     break
#
#     if not FindFlag: # slit为空（遍历为所有可能）时，标志仍为0
#         print("NO")
#
#
# "YES NO YES YES YES NO YES YES YES NO"
# #%%
# # t = int(input())
# t = 1
# for _ in range(t):
#     # n, k = list(map(int, input().split()))
#     # li = list(map(int, input().split()))
#     t = "5 3"
#     n, k = list(map(int, t.split()))
#     h = "6 2 4 3 8"
#     li = list(map(int,h.split()))
#     dp = [[False, 1] for _ in range(n)]
#     dp[0][0] = True
#     for i in range(1, n):
#         flag = False
#         max1 = 0
#         for j in range(max(0, i - k), i):
#             if dp[j][0] == False:
#                 continue
#             elif li[j] >= li[i]:
#                 dp[i] = dp[j].copy()
#                 max1 = max(max1, dp[j][1])
#                 dp[i][1] = max1
#                 flag = True
#             elif li[j] < li[i] and not flag and dp[j][1]:
#                 dp[i] = dp[j].copy()
#                 dp[i][1] = 0
#     if dp[-1][0]:
#         print('YES')
#     else:
#         print('NO')


#%%dp
T = int(input())
# T =1
for t in range(T):
    n,k = list(map(int, input().split()))
    h = list(map(int, input().split()))
    # n,k = 5,3
    # h = "6 2 4 3 8"
    # h = list(map(int,h.split()))

    slist = [[False, 1]] * n # 第一列代表能否跳上, 第二列代表是否使用超能力
    slist[0] = [True, 0]
    for i in range(1,n): # 判断是否能站上第i个，能则slist[i][0]=True
        # mmin = 1 # 超能力
        for j in range(max(0,i-k),i):
            if slist[j][0] :
                if h[j] >= h[i]:
                    # slist[i][0] = True
                    # slist[i][1] = min(slist[j][1], slist[i][1])
                    slist[i] = [True, min(slist[j][1], slist[i][1])]
                if h[j] < h[i] and slist[j][1] ==0:
                    # slist[i][0] = True
                    # slist[i][1] = min(slist[j][1]+1, slist[i][1])
                    slist[i] = [True, min(slist[j][1]+1, slist[i][1])]
    if slist[-1][0] == True:
        print("YES")
    else:
16..22
        print("NO")

        

