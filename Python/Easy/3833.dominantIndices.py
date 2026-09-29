# 3833. Count Dominant Indices
# Beats: 17.74%
def dominantIndices(nums):
    count = 0
    for i in range(len(nums)-1):
        if nums[i] > sum(nums[i+1:])/len(nums[i+1:]):
            dominant.append(nums[i])
            count += 1
    return count


nums = [5,4,3]
nums = [4,1,2]
print(dominantIndices(nums))
