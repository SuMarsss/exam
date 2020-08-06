# starting time: 2020年8月6日14:19:43
# terminal time：2020年8月6日15:41:22
import math
t,h = 1,0
def filter_fun(nums):
    nums.sort(key = lambda x:(-x[t], x[h]))
    pre = float("inf")
    li = []
    for i in range(len(nums)):
        if nums[i][h] < pre:
            li.append(nums[i])
            pre = nums[i][h]
    return li

def main():
    N,M,T = list(map(int, input().split()))
    lunch, dinner = [[0,0]],[[0,0]]
    for i in range(N):
        lunch.append(list(map(int, input().split())))
    for i in range(M):
        dinner.append(list(map(int, input().split())))
    lunch = filter_fun(lunch)
    dinner = filter_fun(dinner)
    res = float("inf")
    if lunch[0][1] + dinner[0][1] < T:
        print(-1)
        return
    else:
        # for i in lunch:
        #     target = T - i[t]
        #     l, r = 0, len(dinner)-1
        #     if target > dinner[l][t]:
        #         continue
        #     while l < r:
        #         mid = math.ceil((l + r) / 2)
        #         if target < dinner[mid][t]:
        #             l = mid
        #         elif target > dinner[mid][t]:
        #             r = mid
        #         elif target == dinner[mid][t]:
        #             res = min(res, dinner[mid][h] + i[h])
        #             print(" target: mid= ", mid)
        #             break
        #         if l == r-1:
        #             res =  min(res, dinner[l][h] + i[h])
        #             print("l == r-1: l= ", l)
        #             break
        #         if l == r:
        #             res =  min(res, dinner[l][h] + i[h])
        #             print("l==r: l= ", l)
        #             break
        # print(res)
        p_lunch, p_dinner = 0,len(dinner)-1
        while p_lunch < len(lunch)  and p_dinner > -1:
            if lunch[p_lunch][t] + dinner[p_dinner][t] >= T:
                res = min(res, lunch[p_lunch][h] + dinner[p_dinner][h])
                p_lunch += 1
            else:
                p_dinner -= 1
        print(res)


if __name__ == '__main__':
    main()