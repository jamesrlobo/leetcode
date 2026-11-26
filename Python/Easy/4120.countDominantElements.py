# 4120. Count Dominant Elements
# https://leetcode.com/problems/count-dominant-elements/
# Beats: 23.99%
def countDominantElements(self, nums: list[int]) -> int:
    n = len(nums)
    if n == 1:
        return 1
    output = 0
    for i in range(n):
        if i == 0:
            if nums[i] >= nums[i+1]:
                output += 1
        elif i == n-1:
            if nums[i] >= nums[i-1]:
                output += 1
        else:
            avg = int(nums[i-1] + nums[i+1])/2
            if nums[i] >= avg:
                output += 1
    return output
