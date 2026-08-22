# 852. Peak Index in a Mountain Array
# https://leetcode.com/problems/peak-index-in-a-mountain-array/description/
# Beats:12.03%
# def peakIndexInMountainArray(arr):
#     return arr.index(max(arr))


arr = [0,10,5,2]
print(peakIndexInMountainArray(arr))

# Beats: 8.20%
# def peakIndexInMountainArray(arr):
#     n = len(arr)
#     for i in range(1, n-1):
#         if arr[i-1] < arr[i] and arr[i] > arr[i+1]:
#             return i
#     return 0
