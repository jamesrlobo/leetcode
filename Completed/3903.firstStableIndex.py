# 3903. Smallest Stable Index I
# https://leetcode.com/problems/smallest-stable-index-i/description/
# Beats: 45.58%
def firstStableIndex(nums, k):
    for i in range(len(nums)):
        stability = max(nums[:i+1]) - min(nums[i:])
        if stability <= k:
            return i
    return -1


nums = [5,0,1,4]
k = 3

nums = [3,2,1]
k = 1
print(firstStableIndex(nums, k))
