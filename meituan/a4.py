# -*- coding: utf-8 -*-
# 
def dire(n):
    a, b = 1, 0
    for i in range(1, n + 1):
        if i % 2 == 1:
            a = (3 * b) % 1000000007
            b = a + 1
        else:
            a = (3 * b) % 1000000007
            b = a - 1
    print(a)
    return a


def dp(n):
    preS = 0
    preA = 1
    for i in range(1,n):
        curA = 2 * preA + preS
        curS = 3 * preA
        preA = curA
        preS = curS
    print(preS)
    return preS

for n in range(1,60):

    if dire(n) != dp(n): 
        print(n,"th,Not equal") 
    else: 
        print(n,"nth,same")
