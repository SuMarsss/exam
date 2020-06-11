# -*- coding: utf-8 -*-

input = [[3,6],[2,5],[8,11],[13,16]]


input.sort(key=lambda x:x[0])
# maxs = -float("inf")
ans = []
maxs = -float("inf") 
tmp = input[0] if input[0] else []
for i in range(len(input)-1):  
    
    if input[i+1][0] <=  tmp[1]:  # 问题2
        # tmp = [tmp[0], input[i+1][1]]
        l = min(tmp[0],input[i+1][0])
        r = max(tmp[1],input[i+1][1])
        tmp = [l, r] 
    else:
        ans.append(tmp)
        tmp = input[i+1]
ans.append(tmp)
