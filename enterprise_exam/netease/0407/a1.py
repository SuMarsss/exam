# -*- coding: utf-8 -*-
n = int(input())
nums = list(map(int,input().split()))

#n = 4
#nums=[1,3,7,15]
Flag = 1
dnums = [0]*(n-1)
for i in range(n-1):
    dnums[i]=nums[i+1] - nums[i]
    if dnums[i] <=0:
        Flag = 0
        print(-1)
        break

def gcd(*num):
    gcd1 = []
    c = 0
    for i in range(1, sorted(num)[0]+1):
        for index, j in enumerate(num):
            c += 1
            if c > 1e10:
                return -1
            if j%i == 0:
                if (index + 1) == len(num):
                    gcd1.append(i)
                    break
                continue
            else:
                break
    
    if not gcd1:
        return -1
    else:
        return sorted(gcd1)[-1]
if Flag == 1: 
    ans = gcd(*dnums)
    print(ans)