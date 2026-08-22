# 941. Valid Mountain Array
# Beats: 57.64%
def validMountainArray(arr):
    if len(arr) < 3:
        return False
    maximum = 0
    if arr.index(max(arr)) == 0 or arr.index(max(arr)) == len(arr):
        return False
    for i in range(len(arr)-1):
        # print(arr[i], arr[i+1])
        if arr[i] == arr[i+1]:
            return False
        elif arr[i] > arr[i+1]:
            maximum = i
            break
    for j in range(maximum+1, len(arr)-1):
        # print(arr[j], arr[j+1])
        if arr[j] <= arr[j+1]:
            return False
    return True


# arr = [2,1]
# arr = [3,5,5]
# arr = [0,3,2,1]
# arr = [9,8,7,6,5,4,3,2,1,0]
arr = [1,1,1,1,1,1,1,2,1]
print(validMountainArray(arr))
