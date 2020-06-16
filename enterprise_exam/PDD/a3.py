N = int(input())
K = int(input())

curA,curB,pre = [0,0],[0,0],[0,1]
ans = "B"
q = [(pre,ans)]
while q:
    pre,ans = q.pop()

    q.append(((pre[0] + pre[1],pre[1]),"A"+ans))
    if pre[0] + pre[1] == K:
        ans = "A" + ans
        break


    q.append(((pre[0],pre[1] + 1), "B"+ans))

if not q:
    ans = "-"
else:
    size =len(ans)
    pres = "B" * (7-size)
    ans = pres + ans

print(ans)