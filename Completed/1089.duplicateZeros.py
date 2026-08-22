# 1089. Duplicate Zeros
def duplicateZeros(arr):
    print(arr)
    i = 0
    while i < len(arr):
        if arr[i] == 0:
            arr.insert(i+1, 0)
            arr.pop()
            i+=1
        i+=1
    return arr



arr = [1,0,2,3,0,4,5,0]
# arr = [1,2,3]
# arr = [0,4,1,0,0,8,0,0,3]
print(duplicateZeros(arr))
