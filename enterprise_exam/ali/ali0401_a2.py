# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 23:14:54 2020

@author: Mat_Laptop
"""
monster = [3, 2, 4]
arrow = [(1, 2), (2, 4), (5, 6), (7, 3), (8, 6)]
def solution(m,a):
# 第一列攻击，第二列蓝
    m.sort(reverse=True) # 递减
    a.sort(key=lambda y : y[0]) # 第0列递增
    ans = 0
    for hp in m:
        alen = len(a)
        for a_ind, (att, _) in enumerate(a):
            if att >= hp :           #找到弓箭
                _,mana = min(a[a_ind:], key=lambda y: y[1])
                mana_ind = a.index((_,mana))
                a.pop(mana_ind)
                ans += mana
                break
            elif a_ind == alen -1:
                print("No1")
                return False
    print(ans)
    return ans
solution(monster[:],arrow[:])

# PriorityQueue 优先队列法
from queue import PriorityQueue
def pq_solution(m,a):
    m.sort(reverse=True) # 递减
    a.sort(reverse=True, key=lambda y : y[0]) # 第0列递减
    pq = PriorityQueue()
    ans = 0
    for mHP in m:
        startFlag = 1
        for att, mana in a[:]:
            # if startFlag and att<mHP:
            #     startFlag=0
            #     print("No")
            #     return False
            if att>=mHP:
                # ind = a.index((att, mana))
                a.pop(0)
                pq.put((mana, att))
            else:
                ans += pq.get()[0]
                break
    print(ans)
    return ans
pq_solution(monster[:],arrow[:])

tlist = [62,41,30,28,16,22,12]
pq = PriorityQueue()
for i in tlist:
    pq.put(-i)

for i in range(len(pq.queue)):
    pq.queue[i] += -i


# pq.queue = pq.queue +[1]*len(pq.queue )

