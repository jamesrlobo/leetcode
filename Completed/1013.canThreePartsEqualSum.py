# 1013. Partition Array Into Three Parts With Equal Sum
# Beats: 55.93%
def canThreePartsEqualSum(arr):
    total = sum(arr)
    if total%3 != 0:
        return False
    target = total//3
    temp, count = 0, 0
    for i in range(len(arr)):
        temp += arr[i]
        if temp == target:
            count += 1
            temp = 0
    return count >= 3

arr = [0,2,1,-6,6,-7,9,1,2,0,1]
arr = [0,2,1,-6,6,7,9,-1,2,0,1]
arr = [3,3,6,5,-2,2,5,1,-9,4]
arr = [0,0,0,0]
print(canThreePartsEqualSum(arr))
