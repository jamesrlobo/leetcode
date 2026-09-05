# 3904. Smallest Stable Index II
# https://leetcode.com/problems/smallest-stable-index-ii/description/
# Beats: 28.64%
def firstStableIndex(nums, k):
    n = len(nums)
    rev_nums = nums[::-1]
    prefMax = -1
    suffMin = [nums[-1]]
    output = []
    for j in range(1, n):
        suffMin.append(min(suffMin[-1], rev_nums[j]))
    suffMin = suffMin[::-1]
    for x in range(n):
        prefMax = max(prefMax, nums[x])
        temp = prefMax - suffMin[x]
        if temp <= k:
            output.append(x)
    if output:
        return min(output)
    return -1


nums = [5,0,1,4]
k = 3
nums = [3,2,1]
k = 1
nums = [0]
k = 0
print(firstStableIndex(nums, k))
