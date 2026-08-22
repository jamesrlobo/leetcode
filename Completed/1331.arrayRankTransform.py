# 1331. Rank Transform of an Array
# https://leetcode.com/problems/rank-transform-of-an-array/description/
# Beats: 96.21%
def arrayRankTransform(arr):
    d = {}
    rank = 1
    result = []
    for val in sorted(set(arr)):
        d[val] = rank
        rank += 1
    for value in arr:
        result.append(d[value])
    return result


# arr = [40,10,20,30]
# arr = [100,100,100]
arr = [37,12,28,9,100,56,80,5,12]
print(arrayRankTransform(arr))
