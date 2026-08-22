# 219. Contains Duplicate II
# Beats: 98.83%
def containsNearbyDuplicate(nums, k):
    d = {}
    for i in range(len(nums)):
        if nums[i] in d and (abs(i - d[nums[i]]) <= k):
            return True
        d[nums[i]] = i
    return False


# nums = [1,2,3,1]
# k = 3
# nums = [1,0,1,1]
# k = 1
nums = [1,2,3,1,2,3]
k = 2
print(containsNearbyDuplicate(nums, k))
