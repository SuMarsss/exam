# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 20:08:24 2020

@author: Mat_Laptop
"""

#n,D = list(map(int,input().split()))
#atts = list(map(int,input().split()))
#vals = list(map(int,input().split()))

D = 50
atts = [100,89,54,50,46,48]
vals = [100,89,54,50,46,48]
n = len(vals)
nums = [(atts[i],vals[i]) for i in range(n)]

ans = 0
nums.sort(key=lambda x:x[0])

aLen = len(atts)
lp = 0
hp = aLen -1

while True:
    lp_temp = lp
    for it in range(lp,hp+1):
        if nums[it][0]< D:
             D +=1
             lp_temp += 1
        else:
            break
    lp = lp_temp   
#    if lp == hp-1:
#        if nums[hp][0]>=D:
#            ans += nums[hp][1]
#            lp = hp
            
    nl = hp - (lp) 
    hp_temp = hp
    
    if lp > hp:
        break

    for it in range(hp,lp-1,-1):
        
        if nums[it][0] >=D+nl:
            ans += nums[it][1]
            D += 1
            nl -= 1
            hp_temp -= 1
        else :       
            break
    
    hp = hp_temp
    
    if lp == hp:
        break

print(ans)
        

    
        