# -*- coding: utf-8 -*-
T = int(input())
n,k = list(map(int,input().split()))
nums = [0]*n
for i in range(n):
    nums[i] = list(map(int,input().split()))
    
mmax = 0
pos = [0,0]
slist = [pos]


Flags = [0]*n
Flag = [False for i in range(n)]
for i in range(n):
    Flags[i]=Flag
    
Flags[0][0] = nums[0][0]
val = 0   

while slist:
    row,col = slist.pop(-1)
    findF = 0  
    for i in range(1,k+1):
        
        if row-k>=0 and row-k<n:
            if nums[row][col]<nums[row-k][col]:#down
                if nums[row][col]+nums[row-k][col]>Flags[row-k][col]:
                    Flags[row-k][col] = nums[row][col]+nums[row-k][col]
                    slist.append((row-k,col))
                    findF = 1
        if row+k>=0 and row+k<n:        
            if nums[row][col]<nums[row+k][col]:#up
                if nums[row][col]+nums[row-k][col]>Flags[row-k][col]:
                    Flags[row+k][col] = nums[row][col]+nums[row+k][col]
                    slist.append((row-k,col))
                    findF = 1
        if col-k>=0 and col-k<n: 
            if nums[row][col]<nums[row][col-k]:#left
                if nums[row][col]+nums[row-k][col]>Flags[row-k][col]:
                    Flags[row][col-k] = nums[row][col]+nums[row][col-k]
                    slist.append((row-k,col))
                    findF = 1
        if col+k>=0 and col+k<n:
            if nums[row][col]<nums[row][col+k]:#right
                if nums[row][col]+nums[row-k][col]>Flags[row-k][col]:
                    Flags[row][col+k] = nums[row][col]+nums[row][col+k]
                    slist.append((row-k,col))
                    findF = 1
            
    if findF == 0:
            val = Flags[row][col] 
   
print(val)   
    
