# -*- coding: utf-8 -*-
#x = int(input())
#stime = input()
#n = int(input())

x = 2
stime = "02:01"
n = 24*60*7

# "stime" -> min

intTime = list(map(int,stime.split(":")))
nowTime = intTime[0]*60 + intTime[1]

while 1:
    if nowTime - n >= 0: # 当天时间够
        ansDay = x
        ansTime = nowTime-n
        ansHour = "{}".format(ansTime//60)  if ansTime//60 >= 10 else "0{}".format(ansTime//60) 
        ansMin = "{}".format(ansTime%60) if ansTime%60 >= 10 else "0{}".format(ansTime%60) 
        ansTime = ansHour+":"+ansMin
        break
    elif nowTime - n < 0: # 当天时间不够
        if x > 1: # 这周时间不够
            x -= 1
        else:
            x = 7
        n = n - nowTime
        nowTime = 24*60

print(ansDay)
print(ansTime)