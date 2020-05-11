# -*- coding: utf-8 -*-
T = int(input())
for _ in range(T):
    N,M = list(map(int,input().split()))
    ops = [[0,0].copy() for i in range(M) ] 
#    ops = [[0,0].copy * M]
    for i in range(M):
        temp = list(map(int,input().split()))
        ops[i][0] = temp[0]
        ops[i][1] = temp[1:]
        
