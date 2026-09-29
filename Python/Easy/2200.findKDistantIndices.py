# 2200. Find All K-Distant Indices in an Array
# Beats: 41.72%
def findKDistantIndices(nums, key, k):
    index = []
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[j] == key and abs(i-j) <= k:
                index.append(i)
                break
    return index


# nums = [3,4,9,1,3,9,5]
# key = 9
# k = 1

# nums = [2,2,2,2,2]
# # key = 2
# # k = 2

nums = [3,4,9,1,3,9,5]
key = 9
k = 1
print(findKDistantIndices(nums, key, k))
