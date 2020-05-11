# -*- coding: utf-8 -*-
#n = int(input())
#preOrder = list(map(int,input().split()))
#curOrder = list(map(int,input().split()))
# 排序法
n = 5

preOrder = list(map(int,"5 3 1 4 2 ".split()))
curOrder = list(map(int,"2 4 5 1 3".split()))

s2 = [0]*n
    
pair = {}
for i in range(n):
    pair.update({preOrder[i]:i})
    
for i in range(n):
    s2[i] = pair[curOrder[i]]    
    
c = 0
mmin = s2[n-1]   
for i in range(n-2, -1 ,-1):
#    print(s2[i],min)
    if s2[i] > mmin:
        c += 1
    else:
        mmin = s2[i]
print(c)

