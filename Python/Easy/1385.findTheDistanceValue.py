# 1385. Find the Distance Value Between Two Arrays
# https://leetcode.com/problems/find-the-distance-value-between-two-arrays/description/
# Beats: 13.69%
def findTheDistanceValue(arr1, arr2, d):
    count = 0
    arr2 = sorted(arr2)
    for i in arr1:
        for j in arr2:
            if abs(i-j) <= d:
                break
        else:
            count += 1
    return count


arr1 = [4,5,8]
arr2 = [10,9,1,8]
d = 2

arr1 = [2,1,100,3]
arr2 = [-5,-2,10,-3,7]
d = 6
print(findTheDistanceValue(arr1, arr2, d))
