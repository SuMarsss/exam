# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 16:32:12 2020

@author: Mat_Laptop
"""

t = 1
for it in range(t):
    n,m,k = list(map(int,"3 3 1".split()))
    poslist = set((1,1))
    c,d = list(map(int,"2 2".split()))
    
    pastSeq = set()
    s = n*m
    totPos = len(poslist)
    if s - totPos < c*d:
        print("NO")
        break    
    else:
        # init
        h_poslist = [(1,1)]
        while h_poslist:
            xh,yh = h_poslist.pop()
            if (xh,yh) not in pastSeq:
                pastSeq.update((xh,yh))
            else:
                continue
            h_xh = xh+c-1
            h_yh = xh+d-1
            
            findFlag = 1
            
            for i in range(xh,h_xh+1):
                for j in range(yh,h_yh+1):
                    if (i,j) in poslist:
                        if i+1+c-1 <= n:
                            h_poslist.append((i+1,yh))
                        if j+1+d-1 <= m:
                            h_poslist.append((xh,j+1))
                        findFlag = 0 
                        break
            if findFlag == 1 :
                print("YES")
                findFlag = 1
                break
        if findFlag == 0:
            print("NO")
            
                 
        
        