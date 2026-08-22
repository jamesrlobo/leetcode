# 1200. Minimum Absolute Difference
# Beats: 15.36%
def minimumAbsDifference(arr):
    output = []
    minAbsDiff = []
    arr = sorted(arr)
    for i in range(len(arr)-1):
        if (arr[i+1]-arr[i]) not in minAbsDiff:
            minAbsDiff.append(arr[i+1]-arr[i])
    minAbsDiff = min(minAbsDiff)
    for j in range(len(arr)-1):
        if (arr[j+1] - arr[j]) == minAbsDiff:
            output.append([arr[j],arr[j+1]])
    return output


# arr = [4,2,1,3]
# arr = [1,3,6,10,15]
arr = [3,8,-10,23,19,-4,-14,27]
print(minimumAbsDifference(arr))
