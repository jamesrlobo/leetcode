# 1346. Check If N and Its Double Exist
def checkIfExist(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j:
                if (arr[j] * 2) == arr[i]:
                    return True
    return False


# arr = [10,2,5,3]
arr = [3,1,7,11]
print(checkIfExist(arr))
