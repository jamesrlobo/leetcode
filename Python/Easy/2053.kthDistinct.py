# 2053. Kth Distinct String in an Array
# Beats: 6.74%
def kthDistinct(arr, k):
    distinct = []
    for i in arr:
        if arr.count(i) == 1:
            distinct.append(i)
    if len(distinct) <= k:
        return ""
    return distinct[k-1]


# arr = ["d","b","c","b","c","a"]
# k = 2
# arr = ["aaa","aa","a"]
# k = 1
arr = ["a","b","a"]
k = 3
print(kthDistinct(arr,k))
