# 3105. Longest Strictly Increasing or Strictly Decreasing Subarray
# Beats: 7.43%
def longestMonotonicSubarray(nums):
    increasing, decreasing = [], []
    for i in range(len(nums)):
        for j in range(i, len(nums)+1):
            if i!=j and len(nums[i:j]) > 0 and len(nums[i:j]) == len(set(nums[i:j])):
                if nums[i:j] == sorted(nums[i:j]):
                    # increasing.append(nums[i:j])
                    increasing.append(len(nums[i:j]))
                if nums[i:j] == sorted(nums[i:j], reverse= True):
                    # decreasing.append((nums[i:j]))
                    decreasing.append(len(nums[i:j]))
    return max(max(increasing),max(decreasing))


nums = [1,4,3,3,2]
nums = [3,3,3,3]
nums = [3,2,1]
print(longestMonotonicSubarray(nums))
