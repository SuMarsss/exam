# -*- coding: utf-8 -*-
T = 1
for _ in range(T):
#    N,M = list(map(int,input().split()))
    N,M = 3,7
    ops = [[0,0].copy() for i in range(M) ] 
#    ops = [[0,0].copy * M]
#    for i in range(M):
#        temp = list(map(int,input().split()))
#        ops[i][0] = temp[0]
#        ops[i][1] = temp[1:]
#    
    ops = [[3, [1]], [1, [1, 2]], [3, [1]], [1, [2, 3]], [3, [1]], [2, [1]], [3, [1]]]
    totLi = [set().copy() for i in range(N)]
    for i,s in enumerate(totLi):
           s.add(i+1)
#           print(s)
    temps = [0]*M    
    i = 0
    for op,nums in ops:
       if op == 1:#merge
           x , y = nums[0],nums[1]
#           sx,sy = totLi[x-1],totLi[y-1]
           temps[i] = [totLi[x-1].union(totLi[y-1])]
#           print(t)
           totLi[x-1] = temps[i]
           totLi[y-1] = temps[i]
           
#           for t in totLi[y-1]:
#               totLi[x-1].add(t)
#           totLi[y-1] = totLi[x-1]
           
#           temps[i] = totLi[x-1].union(totLi[y-1])        
#           totLi[x-1] = temps[i].copy()
#           totLi[y-1] = temps[i].copy()           
#           temps[i][0] = 1
#           print(totLi[x-1],totLi[y-1])
       elif op == 2:#split
           for set_t in totLi:
               set_t.discard(nums[0])# break
           tempSet = set()
           tempSet.add(nums[0])
           totLi[nums[0]-1] = tempSet
           
       elif op==3:
           ind = nums[0] -1
           print(len(totLi[ind]))
       i +=1

    
