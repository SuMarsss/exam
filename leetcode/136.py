nums = [2,2,1]
hash = {}
for i in nums:
    if i not in hash:
        hash.update(i)
    else:
        hash.pop(i)