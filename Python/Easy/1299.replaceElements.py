# 1299. Replace Elements with Greatest Element on Right Side
# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/description/
# Beats: 28.02%
def replaceElements(arr):
    arr = arr[::-1]
    for i in range(1, len(arr)-1):
        arr[i] = (max(arr[i-1], arr[i]))
    arr = arr[::-1]
    arr.pop(0)
    arr.append(-1)
    return arr

arr = [17,18,5,4,6,1]
arr = [400]
print(replaceElements(arr))
