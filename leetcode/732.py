import collections
nums = [
    [1,4],
    [1,2],
    [2,3],
    [2,3],
    [2,4],
    [3,4],
    [4,5],
        ]

intervals = nums
intervals.sort(key=lambda x: x[0])

merged = []
ans = 0
for interval in intervals:
    # 如果列表为空，或者当前区间与上一区间不重合，直接添加
    if not merged or merged[-1][1] <= interval[0]:
        merged.append(interval)
    else:
        # 否则的话，我们就可以与上一区间进行合并
        merged[-1][1] = max(merged[-1][1], interval[1])
        ans += 1




