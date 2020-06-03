nums = [3 , 3]
target = 6

hashmap = {}
for ind, num in enumerate(nums):
    hashmap[num] = ind
for i, num in enumerate(nums):
    j = hashmap.get(target - num)
    if j is not None and i != j:
        print([i,j])
        break