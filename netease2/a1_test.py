# -*- coding: utf-8 -*-
"10 3"
Mapb = ["0 0 0 0 0 0 0 0 0 0",
        "0 0 0 0 0 0 0 0 0 0",
        "0 0 0 0 0 0 0 0 0 0",
        "0 0 0 0 0 0 0 0 0 0",
        "0 0 0 0 2 0 0 0 0 0"]
"0 0 0 0 0 0 0 0 0 0"
"0 0 0 0 0 0 0 0 0 0"
"0 0 0 0 0 0 0 0 0 0"
"0 0 0 0 0 0 0 0 0 0"
"0 0 0 0 2 0 0 0 0 0"
T = 1
for _ in range(T):
    M,L = list(map(int,"10 3".split()))
    maps = [0]*M
    sli = []
    tot = 0
    for i in range(M):
#        maps[i] = list(map(int,input().split()))
        maps[i] = list(map(int,"0 0 0 0 2 0 0 0 0 0".split()))
        for j in range(M):
            if maps[i][j] != 0 :
                sli.append([(i,j),maps[i][j]])
                tot += maps[i][j]
    x,y = list(map(int,"0 3".split()))
    i = 0
    for pos,val in sli:
        xt,yt = pos
        d = ((xt-x) ** 2 + (yt-y) ** 2) ** 0.5
        sli[i][0] = d
        i += 1
        #直接排序，或者优先队列
    sli.sort(key=lambda x:x[0])
    for d,val in sli:
        if d>= M:
            L = tot
            break
        if d <= L:
            L += val
        else:
            break
    print(L)
