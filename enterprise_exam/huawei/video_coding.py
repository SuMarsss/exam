# -*- coding: utf-8 -*-
"""
给定两个字符串，其含义为数字
将两个字符串进行数字级的相加
返回字符串
"""
s1 = "1516"
s2 = "98888"
def str_add(s1,s2):
    size = min(len(s1),len(s2))
    bigger_size = max(len(s1),len(s2))
    s = s1 if len(s1)>len(s2) else s2
    res = ""
    cur_add_flag = 0
    for i in range(0, size):        
        tot_num = int(s1[-1-i]) + int(s2[-1-i]) + cur_add_flag
        pre_add_flag = 0
        if tot_num >= 10:
            pre_add_flag = 1
            tot_num = tot_num - 10
        res = str(tot_num) + res
        cur_add_flag = pre_add_flag
    j = None
    for j in range(bigger_size-size-1,-1,-1):
        if j == bigger_size-size-1:
            tmp = int(s[j]) + cur_add_flag
            res = str(tmp) + res
        else:
            res = str(tmp) + res 
    
    if j ==None and cur_add_flag: 
        res = str(tmp) + res
    return res

ans = str_add(s1,s2)

    
    
        
        
        

