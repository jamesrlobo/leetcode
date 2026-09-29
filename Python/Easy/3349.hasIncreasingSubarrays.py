# 3349. Adjacent Increasing Subarrays Detection I
# Beats: 5.48%
def hasIncreasingSubarrays(nums, k):
    index = []
    for i in range(len(nums)-k+1):
        if (nums[i:i+k]) == sorted(nums[i:i+k]) and len(nums[i:i+k]) == len(set(nums[i:i+k])):
            index.append(i)
    print(index)
    for x in index:
        for y in index:
            if x != y and y-x == k:
                return True
    return False


nums = [2,5,7,8,9,2,3,4,3,1]
k = 3

nums = [1,2,3,4,4,4,4,5,6,7]
k = 5

nums = [5,8,-2,-1]
k = 2

nums = [-15,-13,4,7]
k = 2
print(hasIncreasingSubarrays(nums, k))
