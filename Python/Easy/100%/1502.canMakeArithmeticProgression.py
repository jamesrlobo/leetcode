# 1502. Can Make Arithmetic Progression From Sequence
# Beats: 100.00%
def canMakeArithmeticProgression(arr):
    arr = sorted(arr)
    temp = arr[1] - arr[0]
    for i in range(1, len(arr)-1):
        if temp != arr[i+1] - arr[i]:
            return False
    return True


arr = [3,5,1]
arr = [1,2,4]
print(canMakeArithmeticProgression(arr))
