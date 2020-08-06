from collections import defaultdict

if __name__ == '__main__':
    m = int(input())
    counter = defaultdict(int)
    u, d, l, r, f, b = 0, 1, 2, 3, 4, 5
    for _ in range(m):
        nums = list(map(int, input().split()))
        for idx, val in enumerate(nums):
            if val == 1:
                if idx == u:
                    break
                elif idx == d:
                    nums[u], nums[d] = nums[d], nums[u]
                    nums[f], nums[b] = nums[b], nums[f]
                elif idx == l:
                    nums[u], nums[r], nums[d], nums[l] = nums[l], nums[u], nums[r], nums[d]
                elif idx == r:
                    nums[u], nums[l], nums[d], nums[r] = nums[r], nums[u], nums[l], nums[d]
                elif idx == f:
                    nums[u], nums[b], nums[d], nums[f] = nums[f], nums[u], nums[b], nums[d]
                elif idx == b:
                    nums[u], nums[f], nums[d], nums[b] = nums[b], nums[u], nums[f], nums[d]
                break
        num2f = nums[u] + 1
        if num2f == nums[d]:
            num2f += 1
        for idx, val in enumerate(nums):
            if val == num2f:
                if idx == f:
                    break
                elif idx == b:
                    nums[f], nums[b] = nums[b], nums[f]
                    nums[l], nums[r] = nums[r], nums[l]
                elif idx == l:
                    nums[f], nums[r], nums[b], nums[l] = nums[l], nums[f], nums[r], nums[b]
                elif idx == r:
                    nums[f], nums[l], nums[b], nums[r] = nums[r], nums[f], nums[l], nums[b]
        counter[tuple(nums)] += 1
    ret = [v for k, v in counter.items()]
    ret.sort(reverse=True)
    print(len(ret))
    for v in ret:
        print(v, end= ' ')
