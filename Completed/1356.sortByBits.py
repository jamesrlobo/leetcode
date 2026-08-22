# 1356. Sort Integers by The Number of 1 Bits
# Beats: 19.87%
def sortByBits(arr):
    d = {}
    output = []
    for i in arr:
        if (bin(i)[2:]).count('1') not in d:
            d[(bin(i)[2:]).count('1')] = [i]
        else:
            d[(bin(i)[2:]).count('1')] += [i]
    print(d)
    for j in sorted(d.keys()):
        output += sorted(d[j])
    return output


# arr = [0,1,6,7,8,2,3,4,5]
arr = [1024,512,256,128,64,32,16,8,4,2,1]
print(sortByBits(arr))
