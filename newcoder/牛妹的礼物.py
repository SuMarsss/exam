# -*- coding: utf-8 -*-
class Solution:
#    def selectPresent(self , presentVolumn ):
        # write code here
#        def move(col, row, dire):
#            col_nxt = dire[0] + col
#            row_nxt = dire[1] + row
#            if col_nxt<=N-1 and row_nxt <= M-1:
#                val_nxt = vals[col][row] + presentVolumn[col_nxt][row_nxt]
#                if val_nxt < vals[col_nxt][row_nxt]:
#                    vals[col_nxt][row_nxt] = val_nxt
#                    sli.append((col_nxt, row_nxt))        
#        
#        N = len(presentVolumn)
#        M = len(presentVolumn[0])
#        val = [float("inf")]*M
#        vals = [val.copy() for i in range(N)] 
#        vals[0][0] = presentVolumn[0][0]
#        dires = [(0,1),(1,0),(1,1)]
#        sli = [(0,0)]
#        
#        while sli:
#            col, row = sli.pop(0)
#            for dire in dires:
#                move(col,row,dire)
#        return vals[-1][-1]
#            
    def selectPresent(self , presentVolumn ):
        # write code here
        if not presentVolumn:
            return 0
        N = len(presentVolumn)
        M = len(presentVolumn[0])
#        val = [0]*M
        vals = [([0]*M).copy() for i in range(N)]
        vals[0][0] = presentVolumn[0][0]
        for i in range(1,N):
            vals[i][0] = vals[i-1][0] +  presentVolumn[i][0]
        
        for j in range(1,M):
            vals[0][j] = vals[0][j-1] + presentVolumn[0][j]
        
        for i in range(1,N):
            for j in range(1,M):
                vals[i][j] = min(vals[i-1][j-1],vals[i-1][j], vals[i][j-1]) + presentVolumn[i][j]
        return vals[-1][-1]
ex = [[1,2,3],[2,3,4]]            
ans = Solution().selectPresent(ex)     
print(ans)       
