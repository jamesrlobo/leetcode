# 1287. Element Appearing More Than 25% In Sorted Array
# https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/description/
# Beats: 5.64%
def findSpecialInteger(arr):
    twentyFinePercent = int((len(arr)) * 25 / 100)
    for i in set(arr):
        if arr.count(i) > twentyFinePercent:
            return i
    return


arr = [1,2,2,6,6,6,6,7,10]
arr = [1,1]
print(findSpecialInteger(arr))
