# starting time: 2020年8月2日16:45:06
# terminal time: 2020年8月2日17:49:15
import math
T = int(input())
Ns = []
maxN = 0
res = 0
def bs(l,r):
    global  res
    if l == r:
        res += 1
        return res
    if (l+r)%2 == 0:
        mid = (l + r) // 2 -1
    else:
        mid = (l + r) // 2
        mid = math.ceil(mid)
    res += 1
    bs(l, mid)
    return
#
for _ in range(T):
    N = int(input())
    l,r = 1, N
    res = 0
    bs(l, r)
    print(res)
#
# N=926132445
# l,r = 1, N
# res = 0
# bs(l, r)
# print(res)
