# 1460. Make Two Arrays Equal by Reversing Subarrays
# Beats: 76.68%
def canBeEqual(target, arr):
    if target == arr[::-1]:
        return True
    if sorted(target) == sorted(arr):
        return True
    return False


# target = [1,2,3,4]
# arr = [2,4,1,3]

# target = [7]
# arr = [7]

target = [3,7,9]
arr = [3,7,11]
print(canBeEqual(target, arr))
