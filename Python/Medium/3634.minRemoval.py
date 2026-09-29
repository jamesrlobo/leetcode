# 3634. Minimum Removals to Balance Array
# Beats: 46.50%
def minRemoval(nums, k):
    nums = sorted(nums)
    n = len(nums)
    for i in range(len(nums)):
        j = 0
        while j < len(nums) and nums[j] <= nums[i]*k:
            j += 1
        ans = n - (j - i + 1)
    return ans



nums = [2,1,5]
k = 2
nums = [1,6,2,9]
k = 3
nums = [4,6]
k = 2
nums = nums = [1,34,23]
k = 2
print(minRemoval(nums, k))
