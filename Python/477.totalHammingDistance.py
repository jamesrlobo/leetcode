def hamming(item):
    output = 0
    x = bin(item[0])[2:]
    y = bin(item[1])[2:]
    maximum = max(len(x), len(y))
    x = x.zfill(maximum)
    y = y.zfill(maximum)
    for a,b in zip(x,y):
        if a != b:
            output += 1
    return output

def totalHammingDistance(nums):
    count = 0
    subsets = []
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i < j:
                subsets.append([nums[i], nums[j]])
    for item in subsets:
        count += hamming(item)
    return count


nums = [4,14,2]
nums = [4,14,4]
print(totalHammingDistance(nums))
