# -*- coding: utf-8 -*-
# 双指针法
preOrder = list(map(int,"5 3 1 4 2 6 7".split()))
curOrder = list(map(int,"2 4 5 1 3 7 6".split()))
n = len(preOrder)
indx1,indx2 = 0, 0
s = set()
#for i in range(n):
while indx2 < n and indx1 < n:
    if preOrder[indx1] in s:
        indx1 += 1
        continue
    else:
        while curOrder[indx2] != preOrder[indx1]:
            s.add(curOrder[indx2])
            indx2 += 1
        indx1 += 1
        indx2 += 1
    
print(len(s))
    

