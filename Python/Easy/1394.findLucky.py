# 1394. Find Lucky Integer in an Array
# Beats: 10.79%
def findLucky(arr):
    output = []
    for i in set(arr):
        if arr.count(i) == i:
            output.append(i)
    if len(output) != 0:
        return max(output)
    else:
        return -1


# arr = [2,2,3,4]
# arr = [1,2,2,3,3,3]
arr = [2,2,2,3,3]
print(findLucky(arr))
