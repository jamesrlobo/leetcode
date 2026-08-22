# 1539. Kth Missing Positive Number
# Beats: 5.22%
def findKthPositive(arr):
    missing = []
    maximum = max(arr)
    for i in range(1, maximum):
        if i not in arr:
            missing.append(i)
    if len(missing) == 0 or len(missing) < k:
        for j in range(maximum, maximum+k+1):
            if j not in arr:
                missing.append(j)
    print(missing)
    return missing[k-1]


arr = [2,3,4,7,11]
k = 5

arr = [1,2,3,4]
k = 2

# arr = [5,6,7,8,9]
# k = 9
print(findKthPositive(arr))
