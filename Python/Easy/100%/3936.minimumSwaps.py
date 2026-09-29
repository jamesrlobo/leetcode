# 3936. Minimum Swaps to Move Zeros to End [Copied from solutions]
# https://leetcode.com/problems/minimum-swaps-to-move-zeros-to-end/description/
# Beats: 100.00%
def minimumSwaps(nums):
    a = 0
    n = len(nums)
    count = nums.count(0)
    for i in range(n):
        if nums[i] == 0 and i < n - count:
            a += 1
    return a




nums = [0,1,0,3,12]
print(minimumSwaps(nums))
