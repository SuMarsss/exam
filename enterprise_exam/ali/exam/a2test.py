# -*- coding: utf-8 -*-
# 深度优先搜索
T = 1
n, k =3,1
nums = [0]*n
nums = [[1,2,5],[10,11,6],[12,12,7]]

mmax = 0
pos = [0,0]
slist = [pos]
#Flags = [0]*n
Flag = [-1 for i in range(n)]
Flags = [Flag.copy() for i in range(n)]
Flags[0][0] = nums[0][0]

val = 0  
def move(next_row,next_col):
    if next_row>=0 and next_row<n and next_col>=0 and next_col<n:
        if nums[row][col]<nums[next_row][next_col]:#down
            if nums[row][col]+nums[next_row][next_col]>Flags[next_row][next_col]:
                Flags[next_row][next_col] = Flags[row][col]+nums[next_row][next_col]
                slist.append((next_row,next_col))
                findF = 1         
while slist:
    row,col = slist.pop(-1)
    findF = 0  
    for i in range(1,k+1): 
        move(row-k,col)
        move(row+k,col)
        move(row,col-k)
        move(row,col+k)            
    if findF == 0 and val < Flags[row][col]:
            val = Flags[row][col] 
  
print(val) 


#arr = nums
#N, M = len(arr), len(arr[0])
# 
#dp = [[0]*M for i in range(N)]
# 
#dp[0][0] = arr[0][0]
#for i in range(N):
#    dp[i][0] = dp[i-1][0] + arr[i][0]
#for j in range(M):
#    dp[0][j] = dp[0][j-1] + arr[0][j]
# 
#for i in range(1,N):
#    for j in range(1,M):
#        dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + arr[i][j]
# 
#print( dp[N-1][M-1] )   
