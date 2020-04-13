s1 = list("aoefbdse")
s2 = list("afbedsoe")

n = len(s1)
low,high,smax = 0,0,0
lowst, highst = low,high
flag = 0
j=0
iList = []
for i in range(n):
    if s1[i] == s2[j]:
        iList.append(i)
        j += 1
        
ans = len(s1) - len(iList)
print(ans)



        
    
        