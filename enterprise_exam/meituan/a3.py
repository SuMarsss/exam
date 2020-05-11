# -*- coding: utf-8 -*-
"""给n和k，输出最小的x使得
[x] + [x/k] + [x/k^2] + ...
[x]为向下取整，总有一个时刻[x/k^m]==0，因此求使得前面m项和大于n的最小x。"""


from math import floor,ceil
n ,k = 10,3

def erfen(x):
    sum_all = 0
    item = round(x)
    m = 0
    while item != 0:
        sum_all += item
        m += 1
        item = floor((x/(k ** m)))
    return sum_all
    
x = floor(0.5 * n)
c = 1
#delta = n/(2**c)
while 1:
    # left
    c += 1
    delta = n/(2**c)
    sum_all = erfen(x)
    if sum_all < n:
        x = floor(x + delta)
    elif sum_all > n:
        x = ceil(x - delta)
    elif sum_all == n:
        print(x)
        break
    

ans = -1
for i in range(n // k * (k - 1), n + 1):
    total = 0
    ii = i
    while ii:
        total += ii
        if total >= n:
            ans = i
            break
        ii //= k
    if ans != -1:
        break
print(ans)
