# 3940. Limit Occurrences in Sorted Array
# https://leetcode.com/problems/limit-occurrences-in-sorted-array/description/
# Beats: 24.68%
def limitOccurrences(nums, k):
    n = len(nums)
    output = []
    for i in range(n):
        # print(nums[i])
        if nums[i] not in output:
            if nums.count(nums[i]) >= k:
                for j in range(k):
                    output.append(nums[i])
            else:
                temp = nums.count(nums[i])
                for j in range(temp):
                    output.append(nums[i])
    return output


nums = [1,1,1,2,2,3]
k = 2

nums = [1,2,3]
k = 1
print(limitOccurrences(nums, k))
